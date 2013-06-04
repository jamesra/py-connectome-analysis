'''
Created on May 17, 2013

@author: u0490822
'''

from webclient.json.client import WCFDataServicesJsonObjectClient as Client

endpoint = "http://connectomes.utah.edu/Services/RC1/ConnectomeData.svc"
structureQueryTemplate = "Structures(%dL)"

def SetEndpoint(value):
    global endpoint
    endpoint = value

def __CreateClient(**kwargs):
    client_endpoint = kwargs.get('endpoint', endpoint)
    return Client(client_endpoint)

def GetStructure(ID, **kwargs):
    return __CreateClient(**kwargs).Request(structureQueryTemplate % ID)[0]

def GetChildStructureLinks(ID, **kwargs):
    template = "SelectChildStructureLinks?StructureID='%d'"
    '''Get the structurelinks involving the children of a structure'''
    return __CreateClient(**kwargs).Request(template % ID)

def GetLinkedCollection(URI, **kwargs):
    return __CreateClient(endpoint="").Request(URI)


def StructureLocationLinks(structureID, **kwargs):
    template = "SelectStructureLocationLinks?StructureID='%d'"
    return __CreateClient(**kwargs).Request(template % structureID)


def __appendEdgesFromRequest(request, complete_edge_list):
    request.wait()
    for e in request.objects:
        complete_edge_list.append((e.A, e.B))


def LinksForLocations(locations):
    # Consider using StructureLocationLinks procedure instead, much faster
    complete_edge_list = []
    requests = []
    for loc in locations:
        request = __CreateClient(endpoint=None).AsyncRequest(loc.LocationLinksAURI)
        requests.append(request)

        while len(requests) > 100:
            r = requests.pop(0)
            __appendEdgesFromRequest(r, complete_edge_list)
            del r

    for r in requests:
        __appendEdgesFromRequest(r, complete_edge_list)

    return complete_edge_list



if __name__ == '__main__':
    pass