'''
Created on Jun 20, 2013

@author: u0490822
'''



class ServerObjCache(dict):

    def __init__(self, servergetfunc, **kwargs):
        self.__server_get_func = servergetfunc

    def __getitem__(self, key):

        obj = self.get(key, None)
        if obj is None:
            obj = self.__server_get_func(key)
            self[key] = obj

        return obj