'''
Created on Jul 17, 2013

@author: u0490822
'''


from connectome_analysis.datamodels.cache import serverobjcache
import connectome_analysis.datamodels.queries


class StructurePositionDict(serverobjcache.ServerObjCache):
    '''
    Cache for the approximate position of structures.  Contains objects with X,Y,Z,Radius properties
    '''

    def PopulateAll(self):

        StructureLocations = connectome_analysis.datamodels.queries.GetStructureApproxPositions()

        for sloc in StructureLocations:
            self[sloc.ParentID] = sloc

        return