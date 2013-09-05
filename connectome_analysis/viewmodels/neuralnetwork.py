'''
Created on Jun 4, 2013

@author: James Anderson
'''



class NeuralNetwork(object):
    '''
    classdocs
    '''

    @property
    def graph(self):
        return self._graph

    def __init__(self, graph, scalars=None):
        '''
        Constructor
        '''
        self._graph = graph

