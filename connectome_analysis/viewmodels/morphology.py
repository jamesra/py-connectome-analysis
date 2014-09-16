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

iBBox = enum(MinX=0,
                    MinY=1,
                    MinZ=2,
                    MaxX=3,
                    MaxY=4,
                    MaxZ=5,
                    ID=6)

_morphologyCache = {}

DefaultScalars = np.double([2.18, 2.18, -90])  # nm/pixel of our TEM @ 5000x in microns
DefaultScalars *= 0.001

def Load(structureID, useCache=True, XYZScalars=None):

    if useCache:
        if structureID in _morphologyCache:
            return _morphologyCache[structureID]

    structureLocationsGraph = structurelocations.Load(structureID)
    morphology = Morphology(structureLocationsGraph)


    if useCache:
        _morphologyCache[structureID] = morphology

    return morphology


def correct_scale(points, XYZScalars=None, RadiusScalar=None):
    '''Takes an array of [X,Y,Z,Radius] and scales it'''

    if XYZScalars is None:
        global DefaultScalars
        XYZScalars = DefaultScalars  # nm/pixel of our TEM @ 5000x

    if RadiusScalar is None:
        RadiusScalar = (XYZScalars[0] + XYZScalars[1]) / 2.0

    if points.ndim > 1:

        points[:, 0] *= XYZScalars[0]
        points[:, 1] *= XYZScalars[1]
        points[:, 2] *= XYZScalars[2]

        if points.shape[1] > 3:
            points[:, 3] *= RadiusScalar
    else:
        points[0] *= XYZScalars[0]
        points[1] *= XYZScalars[1]
        points[2] *= XYZScalars[2]

        if points.shape > 3:
            points[3] *= RadiusScalar

    return points


def LocationsBoundingBox(data):
    '''Takes a numpy array with columns [X,Y,Z,Radius,ID]. Returns a single bounding box around all locations
    :return: [MinX MinY MinZ MaxX MaxY MaxZ ID]
    :rtype: numpy.array'''

    return np.swapaxes(np.vstack((data[:, iLoc.X] - data[:, iLoc.Radius],
                   data[:, iLoc.Y] - data[:, iLoc.Radius],
                   data[:, iLoc.Z] - data[:, iLoc.Radius],
                   data[:, iLoc.X] + data[:, iLoc.Radius],
                   data[:, iLoc.Y] + data[:, iLoc.Radius],
                   data[:, iLoc.Z] + data[:, iLoc.Radius],
                   data[:, iLoc.ID])), 0, 1)


class SphereNode():
    '''Contains a numpy array describing position and an optional obj property'''

    def __hash__(self):
        return self.ID

    def __eq__(self, other):
        if isinstance(other, SphereNode):
            return self.ID == other.ID
        else:
            return self.ID == other

    @property
    def X(self):
        return self._LocationArray[iLoc.X]

    @property
    def Y(self):
        return self._LocationArray[iLoc.Y]

    @property
    def Z(self):
        return self._LocationArray[iLoc.Z]

    @property
    def Radius(self):
        return self._LocationArray[iLoc.Radius]

    @property
    def ID(self):
        return self._LocationArray[iLoc.ID]

    @property
    def Array(self):
        '''Returns Location numpy array using the iLoc enum indexing'''
        return self._LocationArray

    @property
    def Obj(self):
        return self._Obj

    def __init__(self, ID, X, Y, Z, Radius, Obj):
        self._LocationArray = np.array([X, Y, Z, Radius, ID])
        self._Obj = Obj

    @classmethod
    def CreateFromLocationObject(cls, location):
        '''Create a morphology node from a location node return by connectomics database'''
        node = SphereNode(location.ID,
                          location.VolumeX,
                          location.VolumeY,
                          location.Z,
                          Location.Radius,
                          location)

        return node

    @classmethod
    def CreateFromArray(cls, location):
        '''Create a morphology node from a numpy array of form [ID X Y Z Radius]'''
        node = SphereNode(location[iLoc.ID],
                                location[iLoc.X],
                                location[iLoc.Y],
                                location[iLoc.Z],
                                location[iLoc.Radius],
                                None)

        return node




class Morphology(object):
    '''
    Represents the morphology of a cell using a graph of position nodes with edges representing physically connected nodes
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
    def Locations(self):
        '''Iterator over nodes of the morphology graph'''
        return self._graph.nodes.iter()

    @property
    def LocationLinks(self):
        return list(nx.edges_iter(self.graph))

    @property
    def graph(self):
        return self._graph

    @property
    def kdtree(self):
        if not hasattr(self, '_kdtree'):
            self._kdtree = None

        if self._kdtree is None:
            mat = self.__create_numpy_matrix(self.graph)
            self._kdtree = kdtree.KDTree(mat[:, iLoc.X:iLoc.Z + 1])

        return self._kdtree

    @property
    def LocationArray(self):
        ''':return: [X,Y,Z,Radius,ID]
           :rtype: numpy.array
        '''
        if self._locationarray is None:
            self._locationarray = self.__create_numpy_matrix(self.graph)

        return self._locationarray

    @property
    def BoundingBox(self):
        bbox = self.LocationBoundingBoxes

        minX = np.min(bbox[:, iBBox.MinX])
        minY = np.min(bbox[:, iBBox.MinY])
        minZ = np.min(bbox[:, iBBox.MinZ])
        maxX = np.max(bbox[:, iBBox.MaxX])
        maxY = np.max(bbox[:, iBBox.MaxY])
        maxZ = np.max(bbox[:, iBBox.MaxZ])

        return np.array([minX, minY, minZ, maxX, maxY, maxZ])

    @property
    def LocationBoundingBoxes(self):
        ''':returns: [ID MinX MinY MinZ MaxX MaxY MaxZ]
           :rtype numpy.array:
        '''
        return LocationsBoundingBox(self.LocationArray)

    @classmethod
    def CreateFromStructureLocationsGraph(cls, graph, scalars=None):
        '''
        :Param networkx.Graph: Graph of structure locations
        :Param array: Array of scalars for each dimension [X Y Z Radius]
        :Return: Morphology object 
        '''
        morph = Morphology()

        if scalars is None:
            global DefaultScalars
            scalars = DefaultScalars  # Use the values for the first rabbit connectome if not specified

        morph._scalars = scalars

        for node in nx.nodes_iter(graph):
            morphnode = SphereNode.CreateFromLocationObject(node)
            morph.graph.add_node(morphnode)

        morph._kdtree = None
        morph.__correct_scale()

    @classmethod
    def CreateFromLocationArray(cls, array, scalars=None):
        '''
        :Param ndarray array: Nx5 array [[ID X Y Z Radius]]
        :Param array: Array of scalars for each dimension [X Y Z Radius] 
        :Return: Morphology object 
        '''
        morph = Morphology()

        if scalars is None:
            global DefaultScalars
            scalars = DefaultScalars  # Use the values for the first rabbit connectome if not specified

        morph._scalars = scalars

        (nRows, nCols) = array.shape

        for iRow in range(0, nRows):
            morphnode = SphereNode.CreateFromArray(array[iRow, :])
            morph.graph.add_node(morphnode)

        morph._kdtree = None
        morph.__correct_scale()

    def __init__(self, scalars=None):
        '''
        Constructor, scalars is a tuple with 3 scalars for the X, Y, Z coordinates
        '''

        self._graph = nx.Graph()
        self._kdtree = None

    def Scale(self, scalars):
        self._scalars = scalars

        self.__correct_scale()


    def __correct_scale(self):

        for n in self._graph.nodes_iter():
            n.VolumeX *= self.XScalar
            n.VolumeY *= self.YScalar
            n.Z *= self.ZScalar
            n.Radius *= self.RadiusScalar

        # The cached _locationarray should be adjusted or cleared if we scaled the graph
        self._locationarray = None


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

    def FindNearestNodes(self, point, numMatches=1):
        '''Return the nearest points to the passed point'''
        (distances, indicies) = self.kdtree.query(point, k=numMatches)

        nodelist = []

        for i in indicies:
            node = self.graph.nodes()[i]
            nodelist.append(node)

        return nodelist

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

        # Check the termial and fork nodes first because we do not want them removed
        for n in self.graph.nodes():
            if not n in self.graph.nodes():
                continue

            if nx.degree(self.graph, n) == 2:
                continue

            self.RemoveOverlappingNeighbors(n)

        # Once we have removed nodes which overlap the terminals and forks we can remove
        # overlapping nodes along a process
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

        neighborlist = list(nx.all_neighbors(self.graph, node))
        neighborsRemoved = False

        for neighbor in neighborlist:
            if not neighbor in self.graph.nodes():
                continue

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


