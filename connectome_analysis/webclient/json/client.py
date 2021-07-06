'''
Created on May 8, 2013

@author: Jamesan
'''

import requests
import logging
import threading
import os
from jsonbasedobject import JSONBasedObject


def urljoin(base, ext):
    if base is None:
        return ext

    if len(base) == 0:  # Empty string for endpoint
        return ext

    if base[-1] == '/':
        return base + ext

    return base + '/' + ext

def request_to_objects(req):
    return req["value"]

def NextPageURL(r):
    '''Returns the URL for the next page of results if it exists.
       The __next entry in the content contains the URL to continue the
       query.'''
    r = r.json()
    if "@odata.nextLink" in r:
        return r["@odata.nextLink"]
    else:
        return None

    # requests.get(next, headers=r.request.headers,
    #             hooks=dict(response=print_items))

class AsyncRequestSession(object):

    def __init__(self, query, callback, **kwargs):
        self.callback = callback  # Function to call when all request data is available
        self.data = []
        self.completed = threading.Event()  # The event that task creators can look at to know if the task completes
        self.__dict__.update(kwargs)

        self.__sendRequest(query)

    def wait(self):
        """Wait for task to complete, return the data from the request"""
        self.completed.wait()
        return self.data

    def __sendRequest(self, query):
        headers = {'accept': 'application/json'}
        r = requests.get(query,
                         headers=headers,
                         hooks=dict(response=self.__OnResponse))

    def __OnResponse(self, request, **kwargs):
        '''Handle a response from the server'''
        if request.status_code != 200:
            logger = logging.getLogger('WebClient')
            logger.error("Request failed with status code: " + str(request.status_code))
            logger.error(request.url)
            self.completed.set()
        else:
            serverObjects = request_to_objects(request.json())
            if isinstance(serverObjects, list):
                self.data.extend(serverObjects)
            else:
                self.data.append(serverObjects)

            nextUrl = NextPageURL(request)
            if nextUrl is not None:
                self.__sendRequest(nextUrl)
            else:
                if not self.callback is None:
                    self.callback(self, self.data)
                self.completed.set()


class WCFDataServicesJSonClient(object):
    '''Returns requests results as list of dictionaries'''

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def Request(self, query):
        url = urljoin(self.endpoint, query)

        session = AsyncRequestSession(url, None)
        return session.wait()

    def AsyncRequest(self, query, callback):
        '''return the json objects which result from appending a query to
        endpoint and sending a request'''
        url = urljoin(self.endpoint, query)

        return AsyncRequestSession(url, callback)


class WCFDataServicesJsonObjectClient(WCFDataServicesJSonClient):
    '''Returns requests results as list of objects with more Python friendly interface'''

    def __init__(self, endpoint):
        super(WCFDataServicesJsonObjectClient, self).__init__(endpoint)

    def Request(self, query):
        jsondictlist = super(WCFDataServicesJsonObjectClient, self).Request(query)
        return self.__ObjectsFromResults(jsondictlist)

    def AsyncRequest(self, query, callback=None):
        '''return the json objects which result from appending a query to
        endpoint and sending a request'''
        url = urljoin(self.endpoint, query)
        session = AsyncRequestSession(url, self.__ConvertingCallback, caller_callback=callback)
        return session

    def __ObjectsFromResults(self, jsondictlist):
        objlist = []
        for jsondict in jsondictlist:
            objlist.append(JSONBasedObject(jsondict))

        return objlist

    def __ConvertingCallback(self, session, data):
        assert(hasattr(session, 'caller_callback'))
        objlist = self.__ObjectsFromResults(data)
        session.objects = objlist
        if not session.caller_callback is None:
            session.caller_callback(session, objlist)


if __name__ == '__main__':

    import json

    client = WCFDataServicesJSonClient("http://websvc1.connectomes.utah.edu/RC1/OData")
    session = client.AsyncRequest("StructureTypes", None)
    for data in session.data:
        print(data["ID"], data["Name"])
    # json.dump({"data" : session.data}, open("./StructureTypes.json", "w"), indent=4, sort_keys=True)

    # client = WCFDataServicesJSonClient("http://websvc1.connectomes.utah.edu/RC1/OData")
    # session = client.AsyncRequest("Structures", None)
    # json.dump({"data" : session.data}, open("./Structures.json", "w"), indent=4, sort_keys=True)

    # client = WCFDataServicesJSonClient("http://websvc1.connectomes.utah.edu/RC1/OData")
    # session = client.AsyncRequest("Locations", None)
    # json.dump({"data" : session.data}, open("./Locations.json", "w"), indent=4, sort_keys=True)
