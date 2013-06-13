'''
Created on Jun 4, 2013

@author: u0490822
'''
import test.test_connectomics.test_model as test_model
import viewmodels.neuralnetwork as nn

import matplotlib.pyplot as plt
import networkx as nx

import views.svg as svg
import os

class NeuralNetworkTest(test_model.ConnectivityGraphTest):

    @property
    def Hops(self):
        return 1

    @property
    def StructureID(self):
        return 180

    def test_writeSVG(self):

        neuralNetwork = nn.NeuralNetwork(self.graph)
        svg.FromNeuralNetwork.Save(neuralNetwork.graph, os.path.join(self.OutputPath, '%d.svg' % self.StructureID))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()