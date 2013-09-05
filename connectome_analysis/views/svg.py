'''
Created on Jun 4, 2013

@author: u0490822
'''

import matplotlib.pyplot as plt
import networkx as nx

class FromNeuralNetwork(object):


    @classmethod
    def __NodeLabel(cls, node):
        if node.Label is None:
            return str(node.ID)
        else:
            return str(node.ID) + "\n" + node.Label

    @classmethod
    def NodeLabels(cls, nodes, __labelFunction=None):
        if __labelFunction is None:
            __labelFunction = FromNeuralNetwork.__NodeLabel

        d = {}
        for n in nodes:
            d[n] = __labelFunction(n)
        return d


    @classmethod
    def Save(cls, graph, path):
        plt.figure()
        # layout = nx.spring_layout(graph, scale=2.0)
        layout = nx.graphviz_layout(graph, 'neato')
        labels = FromNeuralNetwork.NodeLabels(graph.nodes())
        nx.draw_networkx(graph, labels=labels, pos=layout, font_size=3)
        plt.savefig(path)

if __name__ == '__main__':
    pass