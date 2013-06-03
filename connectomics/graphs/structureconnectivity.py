'''
Created on May 17, 2013

@author: Jamesan
'''

import networkx as nx
import connectomics.queries as queries
import copy

def Load(structureID, hops=3, endpoint=None):

    structureConnectivity = StructureConnectivity()
    structure = queries.GetStructure(structureID, endpoint=endpoint)

    structureConnectivity.AddStructure(structure)

    for i in range(0, hops):
        print "Fetching connectivity hop #" + str(i)
        structureConnectivity.GetNextHop()

    return structureConnectivity


class StructureStore(dict):

    def __getitem__(self, key):
        if not key in self.keys():
            structure = queries.GetStructure(key)
            self[structure.ID] = structure

        return super(StructureStore, self).__getitem__(key)


structures = StructureStore()

class StructureConnectivity(nx.MultiDiGraph):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
        super(StructureConnectivity,self).__init__()

        self.nexthopstructures = []

    def NodeInGraph(self, structure):
        return self.has_node(structure)

    def AddStructure(self, structure):

        if self.NodeInGraph(structure):
            return

        assert(structure.TypeID == 1)

        structures[structure.ID] = structure

        self.add_node(structure)
        print "Add Node: " + str(structure.ID)

        # self.nexthopstructures.extend( queries.GetLinkedCollection(structure.ChildrenURI) )
        self.FetchChildStructures(structure)
        self.nexthopstructures.append(structure)

    def FetchChildStructures(self, structure):
        '''Grab the child structure in advance to minimize likely round trips'''
        
        if hasattr(structure, 'childStructures'):
            return structure.childStructures
        
        childstructures = queries.GetLinkedCollection(structure.ChildrenURI)
        for s in childstructures:
            structures[s.ID] = s
        
        structure.childStructures = childstructures


    def GetNextHop(self):

        hopStructures = copy.deepcopy(self.nexthopstructures)
        self.nexthopstructures = []
        links = []
        for s in hopStructures:
            links.extend(queries.GetChildStructureLinks(s.ID))
            # sourceLinks = queries.GetLinkedCollection(s.SourceOfLinksURI)
            # links.extend( queries.GetLinkedCollection(s.SourceOfLinksURI) )
            # targetLinks = queries.GetLinkedCollection(s.TargetOfLinksURI)
            # links.extend( queries.GetLinkedCollection(s.TargetOfLinksURI) )

        for l in links:
            self.AddLink(l)

    def AddLink(self, link):

        sourceStructParentID = structures[link.SourceID].ParentID
        targetStructParentID = structures[link.TargetID].ParentID

        sourceParent = structures[sourceStructParentID]
        targetParent = structures[targetStructParentID]

        AddEdge = False  # If both nodes are already in the graph any edges have already been added
        if not self.NodeInGraph(sourceParent):
            self.AddStructure(sourceParent)
            AddEdge = True

        if not self.NodeInGraph(str(targetStructParentID)):
            self.AddStructure(targetParent)
            AddEdge = True

        if AddEdge:
            print "Add edge: " + str(sourceParent.ID) + " -> " + str(targetParent.ID)
            self.add_edge(sourceParent, targetParent, source=structures[link.SourceID], target=structures[link.TargetID])

