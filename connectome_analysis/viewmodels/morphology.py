'''
Created on May 21, 2013

@author: Jamesan
'''

import numpy as np
from scipy.spatial import kdtree, distance
import networkx as nx
import connectome_analysis.datamodels.graphs.structurelocations as structurelocations
from connectome_analysis.enum import enum

iLoc = enum(X=0,
             Y=1,
             Z=2,
             Radius=3,
             ID=4)

def Load(structureID):
    structureLocationsGraph = structurelocations.Load(structureID)
    morphology = Morphology(structureLocationsGraph)
    return morphology


def correct_scale(points, XYZScalars=None, RadiusScalar=None):
    '''Takes an array of [X,Y,Z,Radius] and scales it'''

    if XYZScalars is None:
        XYZScalars = [2.18, 2.18, -90]

    if RadiusScalar is None:
        RadiusScalar = (XYZScalars[0] + XYZScalars[1]) / 2.0

    points[:, 0] *= XYZScalars[0]
    points[:, 1] *= XYZScalars[1]
    points[:, 2] *= XYZScalars[2]

    if points.shape[1] > 3:
        points[:, 3] *= RadiusScalar

    return points


class Morphology(object):
    '''
    classdocs
    '''

    @property
    def XScalar(self):
        return self._scalars[0]

    @property
    def YScalar(self):
        return self._scalars[1]

    @property
    def ZScalar(self):
        return self._scalars[2]

    @property
    def RadiusScalar(self):
        '''Average the X,Y scalars for radius, they should agree anyway'''
        return (self.XScalar + self.YScalar) / 2.0

    @property
    def graph(self):
        return self._graph


    @property
    def Data(self):
        '''Numpy array of [X,Y,Z,Radius,ID]'''
        return self.__create_numpy_matrix(self._graph)


    def __init__(self, graph, scalars=None):
        '''
        Constructor, scalars is a tuple with 3 scalars for the X, Y, Z coordinates
        '''
        if scalars is None:
            scalars = (2.18, 2.18, -90)  # Use the values for the first rabbit connectome if not specified

        self._scalars = scalars

        self._graph = graph
        self.__correct_scale()
        self.locmatrix = self.__create_numpy_matrix(graph)

    def __correct_scale(self):

        for n in self._graph.nodes_iter():
            n.VolumeX *= self.XScalar
            n.VolumeY *= self.YScalar
            n.Z *= self.ZScalar
            n.Radius *= self.RadiusScalar

        # The locmatrix should be erased if we scaled the graph
        self.locmatrix = None

    def __create_numpy_matrix(self, graph):

        numNodes = 0
        Nodelist = None
        if isinstance(graph, list):
            numNodes = len(graph)
            Nodelist = graph
        else:
            numNodes = graph.number_of_nodes()
            Nodelist = graph.nodes_iter()

        locmatrix = np.zeros((numNodes, 5), dtype=np.float32)

        for i, node in enumerate(Nodelist):
            locmatrix[i, iLoc.X] = node.VolumeX
            locmatrix[i, iLoc.Y] = node.VolumeY
            locmatrix[i, iLoc.Z] = node.Z
            locmatrix[i, iLoc.Radius] = node.Radius
            locmatrix[i, iLoc.ID] = node.ID

        return locmatrix


    def LargestRadiusNode(self):
        '''Find the node with the largest radius'''
        return max(self._graph.nodes_iter(), key=lambda x: x.Radius)

    def BridgeSubgraphs(self, graph, ANodes, BNodes):
        '''Create edges between the closest locations of isolated subgraphs'''

        matA = self.__create_numpy_matrix(ANodes)
        matB = self.__create_numpy_matrix(BNodes)

        AKDTree = kdtree.KDTree(matA[:, iLoc.X:iLoc.Z + 1])

        distances = AKDTree.query(matB[:, iLoc.X:iLoc.Z + 1], k=1)
        index_of_minB = distances[0].argmin()
        index_of_minA = distances[1][index_of_minB]

        NodeA = ANodes[index_of_minA]
        NodeB = BNodes[index_of_minB]

        graph.add_edge(NodeA, NodeB)


    def RemoveBreaks(self):

        listSubgraphNodes = nx.connected_components(self.graph)
        while len(listSubgraphNodes) > 1:
            NodesA = listSubgraphNodes[0]
            NodesB = listSubgraphNodes[1]
            del listSubgraphNodes[1]

            self.BridgeSubgraphs(self.graph, NodesA, NodesB)
            NodesA.extend(NodesB)

        assert(len(nx.connected_components(self.graph)) == 1)

    def RemoveAndBridge(self, node):
        '''Remove a node of degree 2 and create an edge between the neighbors of the deleted nodes'''
        assert(nx.degree(self.graph, node) == 2)
        newEdge = list(nx.all_neighbors(self.graph, node))

        # print "Removing %(removed)d and bridging %(A)d - %(B)d" % {'removed': node.ID, 'A' : newEdge[0].ID, 'B' : newEdge[1].ID}
        self.graph.remove_node(node)
        self.graph.add_edge(*newEdge)

    def RemoveOverlappingLocations(self):

        # print "Starting number of nodes: " + str(len(self.graph.nodes()))

        for n in self.graph.nodes():
            if not n in self.graph.nodes():
                continue

            if nx.degree(self.graph, n) == 2:
                continue

            self.RemoveOverlappingNeighbors(n)

        for n in self.graph.nodes():
            if not n in self.graph.nodes():
                continue

            if nx.degree(self.graph, n) == 2:
                self.RemoveOverlappingNeighbors(n)

        # print "Ending number of nodes: " + str(len(self.graph.nodes()))

    @classmethod
    def Distance(cls, A, B):
        pos_a = np.array([[A.VolumeX, A.VolumeY, A.Z],
                          [B.VolumeX, B.VolumeY, B.Z]])
        return distance.pdist(pos_a)[0]

    def RemoveOverlappingNeighbors(self, node):

        neighborlist = nx.all_neighbors(self.graph, node)
        neighborsRemoved = False

        for neighbor in neighborlist:
            # Do not remove endpoints or forks
            if nx.degree(self.graph, neighbor) != 2:
                continue

            distance = Morphology.Distance(node, neighbor)
            if distance < node.Radius or distance < neighbor.Radius:
                self.RemoveAndBridge(neighbor)
                neighborsRemoved = True

        # Keep repeating until nothing is removed
        if neighborsRemoved:
            self.RemoveOverlappingNeighbors(node)
