'''
Created on Jun 20, 2013

@author: u0490822
'''

import connectome_analysis.datamodels
from connectome_analysis.datamodels import queries

class SubstructureLocations(object):
    '''
    classdocs
    '''

    @classmethod
    def Populate(cls, structureIDs, TypeID=None):
        obj = SubstructureLocations()

        filterArg = None
        if not TypeID is None:
            filterArg = "TypeID eq %dL" % TypeID

        obj.SubStructures = []
        for s in structureIDs:
            if not hasattr(s, 'ChildrenURI'):
                continue

            substructures = queries.GetLinkedCollection(s.ChildrenURI, filter=filterArg)

            if not substructures is None:
                obj.SubStructures.extend(substructures)

        return obj

    def Fetch(self, TypeID):
        dictPositions = {}
        for s in self.SubStructures:
            if s.TypeID == TypeID:
                dictPositions[s.ID] = connectome_analysis.datamodels.StructurePositionCache[s.ID]

        return dictPositions

    def __init__(self):
        '''
        Constructor
        '''

        self.StructureTypes = None