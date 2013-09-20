import unittest
from datetime import datetime
from connectome_analysis.datamodels.graphs import structurelocations, structureconnectivity, morphologyconnectivity
import pickle
import test.testbase
import os

endpoint = "http://connectomes.utah.edu/Services/RC1/ConnectomeData.svc"


class GraphTest(test.testbase.TestBase):


    def setUp(self):
        super(GraphTest, self).setUp()
        self._graph = None

        if not os.path.exists(self.TestCachePath):
            os.makedirs(self.TestCachePath)

        if not os.path.exists(self.TestOutputPath):
            os.makedirs(self.TestOutputPath)

    @property
    def GraphCacheDir(self):
        return os.path.join(self.TestCachePath, 'GraphCache')

    @property
    def StructureID(self):
        '''override to change structureID for a test'''
        raise Exception("Test should define StructureID to operate upon")

    @property
    def GraphName(self):
        raise Exception("Test should define GraphName property")

    @property
    def graphPath(self):
        return os.path.join(self.GraphCacheDir, self.GraphName + '%d.pickle' % self.StructureID)

    def ReadPickledGraphFromDisk(self, path):
        '''Read graph from disk using pickle'''
        graph = None
        if os.path.exists(path):
            with open(path, 'r') as filehandle:
                try:
                    graph = pickle.load(filehandle)
                except:
                    graph = None
                    print("Unable to load graph from pickle file: " + self.graphPath)

        return graph

    def ReadOrCreategraph(self):
        '''Reads graph from disk if it exists or creates it from server'''
        if self._graph is None:
            self._graph = self.ReadPickledGraphFromDisk(self.graphPath)

            if self._graph is None:
                print("Reading graph from server")
                self._graph = self.CreateGraph(self.StructureID)
                print("Done reading graph from server")

                self.SaveVariable(self._graph, self.graphPath)

        self.assertIsNotNone(self._graph, "Could not read or create graph")
        return self._graph

    @property
    def graph(self):
        if self._graph is None:
            self._graph = self.ReadOrCreategraph()

        return self._graph

    def CreateGraph(self, StructureID):
        raise Exception("Test should define CreateGraph method to create graph")


class MorphologyGraphTest(GraphTest):

    @property
    def GraphName(self):
        return "StructureLocations"

    @property
    def StructureID(self):
        '''override to change structureID for a test'''
        return 180

    def CreateGraph(self, StructureID):
        return structurelocations.Load(StructureID)


class ConnectivityGraphTest(GraphTest):

    @property
    def StructureID(self):
        '''override to change structureID for a test'''
        return 476

    @property
    def Hops(self):
        return 2

    @property
    def GraphName(self):
        return "StructureConnectivity"

    def CreateGraph(self, StructureID):
        return morphologyconnectivity.Load(StructureID, hops=self.Hops, endpoint=endpoint)