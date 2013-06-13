import unittest
from datetime import datetime
from datamodels.graphs import structurelocations, structureconnectivity
import pickle
import test.testbase
import os

endpoint = "http://connectomes.utah.edu/Services/RC1/ConnectomeData.svc"

class GraphTest(test.testbase.TestBase):

    def setUp(self):
        super(GraphTest, self).setUp()
        self._graph = None
        
        if not os.path.exists(self.GraphCacheDir):
            os.makedirs(self.GraphCacheDir)

        if not os.path.exists(self.OutputPath):
            os.makedirs(self.OutputPath)

    @property
    def GraphCacheDir(self):
        return os.path.join(self.TestBaseDir, 'GraphCache')

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

    def SavePickledGraphToDisk(self, graph, path):
        with open(path, 'w') as filehandle:
            print("Saving: " + path)
            pickle.dump(graph, filehandle)

    def ReadOrCreategraph(self):
        '''Reads graph from disk if it exists or creates it from server'''
        if self._graph is None:
            self._graph = self.ReadPickledGraphFromDisk(self.graphPath)

            if self._graph is None:
                print("Reading graph from server")
                self._graph = self.CreateGraph(self.StructureID)
                print("Done reading graph from server")

                self.SavePickledGraphToDisk(self._graph, self.graphPath)

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
        return structurelocations.Load(StructureID, endpoint=endpoint)


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
        return structureconnectivity.Load(StructureID, hops=self.Hops, endpoint=endpoint)