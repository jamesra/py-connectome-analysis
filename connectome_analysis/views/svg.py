'''
Created on Jun 4, 2013

@author: u0490822
'''

import matplotlib.pyplot as plt
import networkx as nx
import connectome_analysis.viewmodels.distinctlabels as distinctlabels

def ColorForNode(node):
    label = distinctlabels.UniqueLabel(node.Label)

    if label is None:
        return "gray"

    if 'YAC' in label:
        return "red"
    elif 'GAC' in label:
        return "green"
    elif 'CBb' in label:
        return "cyan"
    elif 'CBa' in label:
        return "darkblue"
    elif 'AC' in label:
        return "purple"
    elif 'BC' in label:
        return "blue"
    elif 'GC' in label:
        return "gold"

    return "gray"

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

        colors = map(ColorForNode, graph.nodes())

        nx.draw_networkx(graph, labels=labels, node_color=colors, font_size=3, pos=layout)  # pos=layout, font_size=3)
        plt.savefig(path)

if __name__ == '__main__':
    pass