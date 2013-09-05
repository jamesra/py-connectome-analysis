'''
Created on May 17, 2013

@author: Jamesan
'''

import networkx as nx
import connectome_analysis.datamodels.queries as queries
import copy

def Load(structureID, hops=3, endpoint=None):

    mcgraph = MorphologyConnectivity()
    structure = queries.GetStructure(structureID, endpoint=endpoint)

    mcgraph.AddStructure(structure)

    for i in range(0, hops):
        print "Fetching connectivity hop #" + str(i)
        mcgraph.GetNextHop()

    mcgraph.AddNodeEdges()

    return mcgraph


class MorphologyConnectivity(nx.MultiDiGraph):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

        super(MorphologyConnectivity, self).__init__()

        self.nexthopstructures = []
        self.structures = {}

    def NodeInGraph(self, structure):
        return self.has_node(structure)

    def AddStructure(self, structure):

        if self.NodeInGraph(structure):
            return

        assert(structure.TypeID == 1)

        self.structures[structure.ID] = structure

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
        # for s in childstructures:
            # self.structures[s.ID] = s

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

        sourceStructParentID = queries.GetStructure(link.SourceID).ParentID
        targetStructParentID = queries.GetStructure(link.TargetID).ParentID

        if sourceStructParentID is None or targetStructParentID is None:
            print "Invalid edge: " + str(link.SourceID) + " -> " + str(link.TargetID)
            return

        sourceParent = queries.GetStructure(sourceStructParentID)
        targetParent = queries.GetStructure(targetStructParentID)

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

    def AddChildStructureSourceEdges(self, struct):
        '''Add edges between existing nodes in the graph where the parent structure is the source'''

        for link in struct.ChildStructureLinks:
            source = queries.GetStructure(link.SourceID)
            sourceStructParentID = source.ParentID
            if sourceStructParentID != struct.ID:
                # To prevent duplication we only add links where our parent structure is the source
                continue

            target = queries.GetStructure(link.TargetID)
            targetStructParentID = target.ParentID

            if sourceStructParentID is None or targetStructParentID is None:
                print "Invalid edge: " + str(link.SourceID) + " -> " + str(link.TargetID)
                return

            sourceParent = queries.GetStructure(sourceStructParentID)

            # We do not want to add nodes to the graph at this point.  If a node occurs here it is outside the graph's requested hops.
            # In the original circuit viz these nodes were included as clear "Ghost nodes" to indicate further connections existed
            if not targetStructParentID in self.structures:
                continue

            targetParent = queries.GetStructure(targetStructParentID)

            print "Add edge: " + str(sourceParent.ID) + " -> " + str(targetParent.ID)

            # Create parent-child structure edge
            if not self.has_edge(sourceParent, source):
                self.add_edge(sourceParent, source, IsParentChildEdge=True, link=None)

            if not self.has_edge(targetParent, target):
                self.add_edge(targetParent, target, IsParentChildEdge=True, link=None)

            # Create edge between child self.structures
            self.add_edge(source, target, IsParentChildEdge=False, link=link, source=queries.GetStructure(link.SourceID), target=queries.GetStructure(link.TargetID))