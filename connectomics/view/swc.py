'''
Created on May 22, 2013

@author: u0490822
'''

import networkx as nx
import logging
import os
from connectomics import enum

SWCType = enum(UNDEFINED=0,
                SOMA=1,
                AXON=2,
                DENDRITE=3,
                APICAL_DENDRITE=4,
                FORK_POINT=5,
                END_POINT=6,
                CUSTOM=7)



class SWCEntry(object):

    @property
    def location(self):
        return self._location

    @property
    def swc_base_type(self):
        '''Allows SOMA, AXON, APICAL_DENDRITE, or DENDRITE'''
        return self._swc_base_type

    @property
    def swc_parent(self):
        return self._swc_parent

    def __init__(self, location, swc_type, swc_parent= -1):
        self._location = location
        self._swc_parent = swc_parent

        self._swc_base_type = swc_type
        assert(self._swc_base_type == SWCType.SOMA or
               self._swc_base_type == SWCType.AXON or
               self._swc_base_type == SWCType.DENDRITE or
               self._swc_base_type == SWCType.APICAL_DENDRITE)

class SWC(object):

    @property
    def NextLineNumber(self):
        return len(self.lines) + 1

    @property
    def NumberOfLocations(self):
        return len(self.lines)

    @property
    def Logger(self):
        return logging.getLogger('SWC')

    def __init__(self, somaNode, axonsbelowsoma=True):
        self.lines = []
        self.LocIDToSwcID = {}
        self.somaNode = somaNode  # The node in the graph which is the soma
        self.AxonsBelowSoma = axonsbelowsoma

    def Save(self, filename):
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(filename, 'w') as filehandle:
            filehandle.writelines(self.lines)

    def contains(self, structure):
        if isinstance(structure, int):
            return structure in self.LocIDToSwcID
        elif hasattr(structure, "ID"):
            return structure.ID in self.LocIDToSwcID
        else:
            assert("Unexpected type in contains")

        return False

    def AddLocation(self, Morphology, entry):

        swc_ID = self.NextLineNumber
        if entry.location.ID in self.LocIDToSwcID:
            self.Logger.error("REPEAT %d: %d" % (swc_ID, entry.location.ID))
            return self.LocIDToSwcID[entry.location.ID]
        else:
            self.Logger.info("%d: %d" % (swc_ID, entry.location.ID))

        self.LocIDToSwcID[entry.location.ID] = swc_ID
        self.lines.append(self._LocationText(entry.location, self.__swc_type_for_node(Morphology, entry), entry.swc_parent))


        return swc_ID

    def _LocationText(self, location, swc_type, swc_parentID):

        swctemplate = "%(swc_ID)d %(swc_type)d %(x)g %(y)g %(z)g %(radius)g %(swc_parentID)d\n"

        if swc_parentID is None:
            swc_parentID = -1

        return swctemplate % {'swc_ID' : self.NextLineNumber,
                               'swc_type' : swc_type,
                               'x' : location.VolumeX,
                               'y' : location.VolumeY,
                               'z' : location.Z,
                               'radius' : location.Radius,
                               'swc_parentID' : swc_parentID}

    def __swc_type_for_node(self, Morphology, entry):
        '''The SWC format convolves classification, such as SOMA, DENDRITE, etc...
           with structure, such as end point, fork point, etc... this replaces
           classification types with structural types when required'''
        adjacentNodes = list(nx.all_neighbors(Morphology.graph, entry.location))

        swc_type = entry.swc_base_type
        if len(adjacentNodes) == 1:
            if self.NumberOfLocations == 0:
                swc_type = SWCType.END_POINT
            elif self.contains(adjacentNodes[0]):
                swc_type = SWCType.END_POINT
        elif len(adjacentNodes) > 2:
            swc_type = SWCType.FORK_POINT

        return swc_type


    def calculate_base_type(self, location):

        if location.Z < self.somaNode.Z and self.AxonsBelowSoma:
            return SWCType.AXON
        else:
            return SWCType.DENDRITE


    def base_type_for_adjacent_node(self, Morphology, location, current_swc_type):

        # We only switch the type when transitioning from SOMA to AXON or DENDRITE
        if not current_swc_type == SWCType.SOMA:
            return current_swc_type

        if not self.__IsSoma(Morphology, location):
            return self.calculate_base_type(location)

        return current_swc_type

    def __IsSoma(self, Morphology, location):
        '''Returns true if the location could be part of the soma'''

        # Hard coding that the location should have 20% of the area of the soma to be considered still part of the soma
        # This is a crude estimate and we should replace this with a tag in the location indicating transitions
        if location.Radius * location.Radius < (self.somaNode.Radius * self.somaNode.Radius) * 0.10:
            return False

        # The soma should not fork, use that as another clue to switch to AXON or DENDRITE typing
        if Morphology.graph.degree(location) > 2:
            return False

        return True


def MorphologyToSWC(Morphology):
    '''Converts a graph of locations and location links to the swc format'''

    queue = []

    startingNode = Morphology.LargestRadiusNode()
    swc = SWC(startingNode)

    queue.append(SWCEntry(startingNode, SWCType.SOMA))

    while len(queue) > 0:
        ProcessQueue(Morphology, swc, queue)

    return swc

def ProcessQueue(Morphology, swc, queue):
    '''Process the first entry on the queue'''
    entry = queue.pop()

    swc_ID = swc.AddLocation(Morphology, entry)

    adjacentNodes = nx.all_neighbors(Morphology.graph, entry.location)

    for node in adjacentNodes:
        if swc.contains(node.ID):
            continue

        linked_swc_type = swc.base_type_for_adjacent_node(Morphology, node, entry.swc_base_type)
        queue.append(SWCEntry(node, linked_swc_type, swc_parent=swc_ID))

    return



if __name__ == '__main__':
    pass