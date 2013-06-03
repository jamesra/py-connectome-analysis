'''
Created on May 16, 2013

@author: u0490822
'''

import datetime

def TryExtractDate(value):

    if not value.startswith('/Date('):
        return None

    try:
        date_val = int(value[6:-2])
    except:
        return None

    return datetime.datetime.utcfromtimestamp(date_val / 1000.0)

def ConvertValue(value, encoding=None):
    '''Convert a string/unicode value to an int, float, or encoded string'''

    if encoding is None:
        encoding = 'UTF-8'

    sval = value.encode(encoding).strip()

    dval = TryExtractDate(sval)
    if not dval is None:
        return dval

    try:
        ival = int(sval)
        return ival
    except:
        pass

    try:
        fval = float(sval)
        return fval
    except:
        pass

    return sval


class JSONBasedObject(object):
    '''
    Creates easier to use objects based on the JSON returned from a WCF Data Services query response
    '''
    
    def __str__(self):
        if hasattr(self, 'ID'):
            return str(self.ID)
        else:
            return super(JSONBasedObject, self).__str__()

    def __hash__(self):
        if hasattr(self, 'ID'):
            return self.ID
        else:
            return super(JSONBasedObject, self).__hash__()

    def __eq__(self, other):
        if hasattr(self, 'type') and hasattr(other, 'type'):
            if self.type != other.type:
                return False

        if hasattr(self, 'ID') and hasattr(other, 'ID'):
            return self.ID == other.ID
        else:
            return False

    def AddDeferedProperty(self, name, value):
        '''Used for links to objects which require a trip to the server'''
        if not '__deferred' in value:
            return

        metadata = value['__deferred']
        uri = metadata['uri']

        setattr(self, name + 'URI', uri)


    def AddProperty(self, name, value):
        '''For fixed value properties converts the type and adds the property.
           Otherwise it adds lazy initializer'''

        if isinstance(value, dict):
            # Deferred property
            self.AddDeferedProperty(name, value)
        elif isinstance(value, str) or isinstance(value, unicode):
            setattr(self, name, ConvertValue(value))
        else:
            setattr(self, name, value)

    def AddMetaData(self, value):
        if 'uri' in value:
            self.SourceURI = value['uri']

        if 'type' in value:
            self.server_type = value['type']

    def __init__(self, attribs):
        '''
        Constructor
        '''

        for k, v in attribs.items():
            if k == '__metadata':
                self.AddMetaData(v)
            elif k[0] == '_':
                continue
            else:
                self.AddProperty(k, v)

