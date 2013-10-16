'''
Created on May 17, 2013

@author: u0490822
'''

from connectome_analysis.webclient.json.client import WCFDataServicesJsonObjectClient as Client
import connectome_analysis.datamodels
import numpy as np

defaultendpoint = "http://connectomes.utah.edu/Services/RC1/ConnectomeData.svc"
structureQueryTemplate = "Structures(%dL)"
structureTypeQueryTemplate = "StructureTypes(%dL)"
structuresOfTypeQueryTemplate = "Structures?$filter=(TypeID eq %dL)"


def SetEndpoint(endpoint):
    global defaultendpoint
    defaultendpoint = endpoint


def __CreateClient(**kwargs):

    client_endpoint = kwargs.get('endpoint', defaultendpoint)
    return Client(client_endpoint)


def GetStructure(ID, **kwargs):
    return connectome_analysis.datamodels.StructureCache[ID]


def GetStructureType(ID, **kwargs):
    return connectome_analysis.datamodels.StructureTypeCache[ID]


def _GetStructure(ID, **kwargs):
    data = __CreateClient(**kwargs).Request(structureQueryTemplate % ID)
    if data is None:
        return None

    if len(data) == 0:
        return None

    return data[0]


def _GetStructureType(ID, **kwargs):
    data = __CreateClient(**kwargs).Request(structureTypeQueryTemplate % ID)

    if data is None:
        return None

    if len(data) == 0:
        return None

    return data[0]


def GetStructuresOfType(TypeID, **kwargs):
    structs = __CreateClient(**kwargs).Request(structuresOfTypeQueryTemplate % TypeID)
    AddObjectCollectionToCache(structs)
    return structs


def GetStructurelocations(structure, **kwargs):
    if kwargs.get('UseCache', True):
        if hasattr(structure, '_locations'):
            return structure._locations

    locations = GetLinkedCollection(structure.LocationsURI)
    structure._locations = locations
    return locations


def GetChildStructureLinks(ID, **kwargs):
    template = "SelectChildStructureLinks?StructureID=%dL"
    '''Get the structurelinks involving the children of a structure'''
    return __CreateClient(**kwargs).Request(template % ID)


def GetStructuresWithLabels(**kwargs):
    template = "Structures?$filter=(length(Label) gt 0)"
    structs = __CreateClient(**kwargs).Request(template)
    AddObjectCollectionToCache(structs)
    return structs

def GetLinkedCollection(URI, **kwargs):

    filterArg = kwargs.get('filter', None)
    if not filterArg is None:
        URI = URI + "?$filter=" + filterArg

    linkedCollection = __CreateClient(endpoint="").Request(URI)

    AddObjectCollectionToCache(linkedCollection)

    return linkedCollection

def AddObjectCollectionToCache(objects):

    for obj in objects:
        if(hasattr(obj, 'server_type')):
           AddObjectToCache(obj)

def AddObjectToCache(obj):
    if obj.server_type == 'ConnectomeModel.Structure':
        connectome_analysis.datamodels.StructureCache[obj.ID] = obj
    elif obj.server_type == 'ConnectomeModel.StructureType':
        connectome_analysis.datamodels.StructureTypeCache[obj.ID] = obj


def GetStructures(URI, **kwargs):
    structures = __CreateClient(**kwargs).Request("Structures")

    global StructureCache
    for s in structures:
        if not s.ID in StructureCache:
            StructureCache[s.ID] = s


def StructureLocationLinks(structureID, **kwargs):
    template = "SelectStructureLocationLinks?StructureID=%dL"
    return __CreateClient(**kwargs).Request(template % structureID)


def GetStructureApproxPosition(structureID, **kwargs):
    obj = connectome_analysis.datamodels.StructurePositionCache[structureID]
    data = np.double([obj.X, obj.Y, obj.Z, obj.Radius])
    return data


def _GetStructureApproxPosition(structureID, **kwargs):
    template = "ApproximateStructureLocation?StructureID=%dL"
    data = __CreateClient(**kwargs).Request(template % structureID)
    if data is None:
        return None

    if len(data) == 0:
        return None

    return data[0]


def GetStructureApproxPositions(**kwargs):
    template = "ApproximateStructureLocations"
    obj = __CreateClient(**kwargs).Request(template)

    datalist = []

    for i in obj:
        datalist.append([i.X, i.Y, i.Z, i.Radius])

    return np.double(datalist)


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