'''
Created on Sept 15 2013

@author: James Anderson

Stuff I think I know about NeuroML and Neuron
cableid attribute is required for <Segment> element
Corresponding <Cable> element for a <Segment> is not required

'''

import networkx as nx
import logging
import os
import xml.etree.ElementTree as etree
import pyxb.utils.domutils
import pyxb

import connectome_analysis.viewmodels.morphology as morphology
from connectome_analysis.enum import enum

# import neuroml.morphology as ml

import neuroml_20b1.nml as nml

nextid = -1

def _getnextid():
    global nextid
    nextid += 1
    return nextid


def CreatePointElement(point):

    elem = None
    if(len(point) == 4):
        elem = nml.Point3DWithDiam()
        elem.diameter = point[3]
    else:
        raise Exception("CreatePointElement only supports lists of [X Y Z Diameter]")

    elem.x = point[0]
    elem.y = point[1]
    elem.z = point[2]
    return elem


def CreateSegmentElement(seg):
    elem = nml.Segment()
    elem.id = seg.ID
    elem.cable = seg.cable

    elem.distal = CreatePointElement([seg.x, seg.y, seg.z, seg.diameter])

    if not seg.parent is None:
        segParent = nml.SegmentParent()
        segParent.segment = seg.parent.ID
        elem.parent = segParent

        elem.proximal = CreatePointElement([seg.parent.x, seg.parent.y, seg.parent.z, seg.parent.diameter])

    # print elem.toxml('utf-8')

    return elem

class segment(object):

    @property
    def ID(self):
        return self._ID

    @property
    def x(self):
        return self._position[0]

    @property
    def y(self):
        return self._position[1]

    @property
    def z(self):
        return self._position[2]

    @property
    def diameter(self):
        return self._diameter

    @property
    def parent(self):
        return self._parent

    @property
    def cable(self):
        return self._cable

    @cable.setter
    def cable(self, val):
        self._cable = val

    def __str__(self):
        string = "ID: %d " % self.ID

        if not self.parent is None:
            string += "parent: %d " % self.parent.ID

        if not self.cable is None:
            string += "cable: %d " % self.cable

        template = "pos: (%(x)d %(y)d %(z)d) dia: %(diameter)f"

        s = template % {"x" : self.x,
                        "y" : self.y,
                        "z" : self.z,
                        "diameter" : self.diameter}

        string += s
        return string

    def __init__(self, ID, position, diameter, parent=None, cable=None):

        # self._ID = _getnextid()
        self._ID = ID
        self._position = position
        self._diameter = diameter
        self._parent = parent
        self._cable = cable


def CreateSegment(nxnode, parent=None, cable=None):
    '''Record information for a neuroml segment element'''

    seg = segment(nxnode.ID, position=[nxnode.VolumeX, nxnode.VolumeY, nxnode.Z], diameter=nxnode.Radius * 2, parent=parent, cable=cable)
    return seg

    # seg = mml.Segment()


def CreateCell(ID, segments):

    cellelem = nml.Cell()

    elem = nml.Morphology()

    elem.id = ID

    for s in segments:
        elem.append(CreateSegmentElement(s))

    cellelem.name = str(ID)
    cellelem.id = ID

    cellelem.morphology = elem

    return cellelem

def CreateDocument(cells):

    root = nml.NeuroMLDocument()

    root.id = 0

    for c in cells:
        root.cell.append(c)

    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(nml.Namespace, "nml")
#    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(mml.Namespace, "mml")
#    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(metaml.Namespace, "meta")

    xml = root.toxml()

    return xml

# def CreateSegment(graph, edge):
#
#    A = edge[0]
#    B = edge[1]
#
#    length = morphology.Morphology.Distance(A, B)
#
#    seg = ml.Segment(length=length, r1=A.Radius, r2=B.Radius)
#
#    return seg


def MorphologyToNeuroML(MorphGraph):
    '''Converts a graph of locations and location links to the swc format'''

    queue = []

    startingNode = MorphGraph.LargestRadiusNode()

    rootseg = CreateSegment(startingNode, cable=_getnextid())

    queue.append((startingNode, rootseg))

    segmentlist = [rootseg]
    processedNodes = {}

    while len(queue) > 0:
        ProcessQueue(MorphGraph, queue, processedNodes, segmentlist)

    print len(segmentlist)

    cellElem = CreateCell(1, segmentlist)

    xml = CreateDocument([cellElem])


    return xml

def ProcessQueue(graph, queue, processedNodes=None, segmentlist=None):
    '''Process the first entry on the queue'''

#    if segmentlist is None:
#        segmentlist = []
#
#    if processedNodes is None:
#        processedNodes = {}

    if len(queue) == 0:
        return segmentlist

    # Queue has tuples of (nx_node, ml_node)
    (nx_node, ml_node) = queue.pop()

    processedNodes[nx_node.ID] = nx_node

    adjacentNodes = nx.all_neighbors(graph.graph, nx_node)

    for node in adjacentNodes:

        if node.ID in processedNodes:
            continue

        mlChildNode = CreateSegment(node, parent=ml_node, cable=_getnextid())
        segmentlist.append(mlChildNode)

        queue.append((node, mlChildNode))

    return segmentlist


if __name__ == '__main__':
    pass