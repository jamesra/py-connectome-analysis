'''
Created on May 17, 2013

@author: Jamesan
'''

import networkx as nx
import connectome_analysis.datamodels.queries as queries
import copy

def Load(structureID, hops=3, endpoint=None):

    structureConnectivity = StructureConnectivity()
    structure = queries.GetStructure(structureID, endpoint=endpoint)

    structureConnectivity.AddStructure(structure)

    for i in range(0, hops):
        print "Fetching connectivity hop #" + str(i)
        structureConnectivity.GetNextHop()

    structureConnectivity.AddNodeEdges()

    return structureConnectivity


class StructureStore(dict):

    def __getitem__(self, key):

        structure = self.get(key, None)
        if structure is None:
            structure = queries.GetStructure(key)
            self[structure.ID] = structure

        return structure


structures = StructureStore()

class StructureConnectivity(nx.MultiDiGraph):
    '''
    A graph showing which cells are connected to other cells with an edge for each synapse
    '''

    def __init__(self):
        '''
        Constructor
        '''

        super(StructureConnectivity, self).__init__()

        self.nexthopstructures = []

    def NodeInGraph(self, structure):
        return self.has_node(structure)

    def AddStructure(self, structure):

        if self.NodeInGraph(structure):
            return

        assert(structure.TypeID == 1)

        structures[structure.ID] = structure

        self.add_node(structure)

        helpstr = "Add Node: " + str(structure.ID)
        if structure.Label is not None:
            helpstr += " " + structure.Label

        print helpstr

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
            s.ChildStructureLinks = queries.GetChildStructureLinks(s.ID)
            links.extend(queries.GetChildStructureLinks(s.ID))
            # sourceLinks = queries.GetLinkedCollection(s.SourceOfLinksURI)
            # links.extend( queries.GetLinkedCollection(s.SourceOfLinksURI) )
            # targetLinks = queries.GetLinkedCollection(s.TargetOfLinksURI)
            # links.extend( queries.GetLinkedCollection(s.TargetOfLinksURI) )

        for l in links:
            self.AddHopNodes(l)


    def AddHopNodes(self, link):
        '''Add nodes only based on the links we discovered'''

        sourceStructParentID = structures[link.SourceID].ParentID
        targetStructParentID = structures[link.TargetID].ParentID

        if sourceStructParentID is None or targetStructParentID is None:
            print "Invalid edge: " + str(link.SourceID) + " -> " + str(link.TargetID)
            return

        sourceParent = structures[sourceStructParentID]
        targetParent = structures[targetStructParentID]

        if not self.NodeInGraph(sourceParent):
            self.AddStructure(sourceParent)

        if not self.NodeInGraph(str(targetStructParentID)):
            self.AddStructure(targetParent)


    def AddNodeEdges(self):
        '''Once all nodes are populated add the links between the nodes'''

        for struct in self.nodes():
            if not hasattr(struct, 'ChildStructureLinks'):
                struct.ChildStructureLinks = queries.GetChildStructureLinks(struct.ID)

            self.AddChildStructureSourceEdges(struct)

    def _CreateEdgeKey(self, sourceID, targetID):

        if sourceID < targetID:
            return "%d-%d" % (sourceID, targetID)
        else:
            return "%d-%d" % (targetID, sourceID)

    def AddChildStructureSourceEdges(self, struct):
        '''Add edges between existing nodes in the graph where the parent structure is the source'''

        for link in struct.ChildStructureLinks:
            sourceStructParentID = structures[link.SourceID].ParentID
            if sourceStructParentID != struct.ID:
                # To prevent duplication we only add links where our parent structure is the source
                continue

            targetStructParentID = structures[link.TargetID].ParentID

            if sourceStructParentID is None or targetStructParentID is None:
                print "Invalid edge: " + str(link.SourceID) + " -> " + str(link.TargetID)
                return

            sourceParent = structures[sourceStructParentID]

            edgekey = self._CreateEdgeKey(link.SourceID, link.TargetID)

            # We do not want to add nodes to the graph at this point.  If a node occurs here it is outside the graph's requested hops.
            # In the original circuit viz these nodes were included as clear "Ghost nodes" to indicate further connections existed
            if not targetStructParentID in structures:
                continue

            targetParent = structures[targetStructParentID]

            sourceStruct = structures[link.SourceID]
            sourceType = queries.GetStructureType[sourceStruct.TypeID]

            print "Add edge: " + str(sourceParent.ID) + " -> " + str(targetParent.ID) + " [" + sourceType.Name + "]"
            self.add_edge(sourceParent, targetParent, key=edgekey, link=link, source=structures[link.SourceID], target=structures[link.TargetID], type=sourceType)