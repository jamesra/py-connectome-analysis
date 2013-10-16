'''
Created on May 16, 2013

@author: u0490822
'''

import networkx as nx
import connectome_analysis.datamodels.queries as queries
import connectome_analysis.datamodels

def Load(structureID):

    structure = queries.GetStructure(structureID)
    locations = queries.GetLinkedCollection(structure.LocationsURI)

    connGraph = StructureLocations(structure, locations)

    return connGraph

class StructureLocations(nx.Graph):
    '''An unfiltered graph containing all locations for a structure'''

    @property
    def ID(self):
        return self.structure.ID

    @property
    def structure(self):
        return self._structure

    def __init__(self, structure, locations, **kwargs):
        '''
        build a graph of the morphology for a structure
        '''
        super(StructureLocations, self).__init__(structure=structure)
        self._structure = structure
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

        edge_tuples = []

        for e in edges:
            if not e.A in self.structureDict:
                print "Missing structure, bad parent? " + str(e.A) + "-" + str(e.B)
                continue

            if not e.B in self.structureDict:
                print "Missing structure, bad parent? " + str(e.B) + "-" + str(e.A)
                continue

            edge_tuples.append((self.structureDict[e.A], self.structureDict[e.B], e.__dict__))

        # edge_tuples = [(self.structureDict[e.A], self.structureDict[e.B], e.__dict__) for e in edges]
        self.add_edges_from(edge_tuples)
