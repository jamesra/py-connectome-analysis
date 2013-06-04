'''
Created on May 16, 2013

@author: u0490822
'''

import networkx as nx
import datamodels.queries as queries

def Load(structureID, endpoint=None):

    structure = queries.GetStructure(structureID, endpoint=endpoint)
    locations = queries.GetLinkedCollection(structure.LocationsURI)

    connGraph = StructureLocations(structure, locations)

    return connGraph

class StructureLocations(nx.Graph):
    '''An unfiltered graph containing all locations for a structure'''

    def __init__(self, structure, locations, **kwargs):
        '''
        build a graph of the morphology for a structure
        '''
        super(StructureLocations, self).__init__(structure=structure)
        self.__BuildGraph(structure, locations)

    def __BuildGraph(self, structure, locations):
        '''
        build a graph of the morphology for a structure
        '''

        # Create nodes for each location
        self.structureDict = {}
        for loc in locations:
            self.add_node(loc)
            self.structureDict[loc.ID] = loc

        edges = queries.StructureLocationLinks(structure.ID)
        edge_tuples = [(self.structureDict[e.A], self.structureDict[e.B], e.__dict__) for e in edges]
        self.add_edges_from(edge_tuples)
