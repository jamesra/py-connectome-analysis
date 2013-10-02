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
import connectome_analysis.viewmodels.distinctlabels as distinctlabels
import connectome_analysis.datamodels.queries as queries
from connectome_analysis.enum import enum

# import neuroml.morphology as ml

import neuroml_18.morph as mml
import neuroml_18.metaml as metaml
import neuroml_18.nml as nml
import neuroml_18.net as net

pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(nml.Namespace, "nml")
pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(mml.Namespace, "mml")
pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(metaml.Namespace, "meta")

nextcableid = -1

logger = logging.getLogger("neuromlview")


def _getnextcableid():
    global nextcableid
    nextcableid += 1
    return nextcableid


def CreatePointElement(point):

    elem = None
    if(len(point) == 4):
        elem = metaml.Point()
        elem.diameter = point[3]
    elif(len(point) == 3):
        elem = metaml.Point3D()

    elem.x = point[0]
    elem.y = point[1]
    elem.z = point[2]
    return elem


def CreateSegmentElement(seg):
    elem = mml.Segment()
    elem.id = seg.ID
    elem.cable = seg.cable

    elem.distal = CreatePointElement([seg.x, seg.y, seg.z, seg.diameter])

    if not seg.parent is None:
        elem.parent = seg.parent.ID
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


def CreateCell(ID, segments):

    elem = nml.Level3Cell()
    elem.segments = pyxb.BIND()
    for s in segments:
        elem.segments.append(CreateSegmentElement(s))

    elem.name = str(ID)

    return elem


def CreateDocument():

    root = nml.neuroml()

    return root


def MorphologyToCell(MorphGraph):

    queue = []

    startingNode = MorphGraph.LargestRadiusNode()

    rootseg = CreateSegment(startingNode, cable=_getnextcableid())

    queue.append((startingNode, rootseg))

    segmentlist = [rootseg]
    processedNodes = {}

    while len(queue) > 0:
        ProcessQueue(MorphGraph, queue, processedNodes, segmentlist)
        
      # Use push instead of append because Neuron wants cableid's to be adjacent in the XML
    segmentlist.sort(key=lambda segment: int(segment.cable))

#    print len(segmentlist)

    cellElem = CreateCell(MorphGraph.graph.ID, segmentlist)
    return cellElem


def MorphologyToNeuroML(MorphGraph):
    '''Converts a graph of locations and location links to the swc format'''

    neuroml_elem = CreateDocument()
    cells = MorphologyToCell(MorphGraph)
    neuroml_elem.cells = pyxb.BIND()
    neuroml_elem.cells.append(cells)

    return neuroml_elem


def CreateCells(morphologylist):

    cells = pyxb.BIND()

    for morphgraph in morphologylist:
        cell_elem = MorphologyToCell(morphgraph)
        cells.append(cell_elem)

    return cells


def CreatePopulations(neuroml, morphconngraph):

    populations = net.Populations()

    instance = net.Instances()

    for n in morphconngraph.nodes():
        pop = net.Population()

        pop.instances = pyxb.BIND()

        populations.append(pop)

        pop.name = n.ID

        if not n.Label is None:
            pop.cell_type_ = distinctlabels.UniqueLabel(n.Label)
        else:
            pop.cell_type_ = "Unknown"

        instance = net.CellInstance()
        instance.id = 0
        location = CreatePointElement([0, 0, 0])
        instance.location = location

        pop.instances.append(instance)
        pop.instances.size = len(pop.instances.instance)

    logger.info(populations.toxml())
    return populations


def FindProjection(projections, sourceid, targetid):
    for proj in projections.projection:
        if proj.source == sourceid and proj.target == targetid:
            return proj

    return None


def CreateConnection(morphconngraph, edge):
    SourceCell = edge[0]
    TargetCell = edge[1]

    edgedata = _GetEdgeData(morphconngraph, edge)

    SourcePosition = queries.GetStructureApproxPosition(edgedata['source'].ID)
    TargetPosition = queries.GetStructureApproxPosition(edgedata['target'].ID)

    SourcePosition = morphology.correct_scale(SourcePosition)
    TargetPosition = morphology.correct_scale(TargetPosition)

    print str(edgedata['source'].ID) + " : " + str(SourcePosition)
    print str(edgedata['target'].ID) + " : " + str(TargetPosition)

    conn = net.Connection()
    conn.id = "0"
    conn.pre_cell_id = SourceCell.ID
    conn.post_cell_id = TargetCell.ID

    (pre_segmentid, pre_fraction) = GetSegmentIdAndFraction(SourceCell.ID, SourcePosition[0:3])
    (post_segmentid, post_fraction) = GetSegmentIdAndFraction(TargetCell.ID, TargetPosition[0:3])

    conn.pre_segment_id = pre_segmentid
    conn.post_segment_id = post_segmentid
    conn.pre_fraction_along = pre_fraction
    conn.post_fraction_along = post_fraction

#    print conn.toxml()

    return conn


def GetSegmentIdAndFraction(cellid, position):

    morphGraph = morphology.Load(cellid)

    # Find the two nearest nodes, if they are linked then calculate the percentage.  If they are not then assume the nearest point is the location of the link.

    nodes = morphGraph.FindNearestNodes(position[0:3], numMatches=2)

    closest_node = nodes[0]
    second_node = nodes[1]

    neighbors = nx.all_neighbors(morphGraph.graph, closest_node)

    fraction = 0.0
    # if second_node in neighbors:
        # Calculate the fraction


    return (closest_node.ID, fraction)


def _GetEdgeData(morphconngraph, edge):

    # If edge doesn't have three values it was probably fetched from networkx without using data=True
    if len(edge) < 3:
        val = morphconngraph.edges(edge, data=True)[0]
        return val[2]
    else:
        return edge[2]


def _SynapseWeight(source, target):
    '''Take the minimum area of the source or target'''

    src_pos = queries.GetStructureApproxPosition(source.ID)
    target_pos = queries.GetStructureApproxPosition(target.ID)

    src_pos = morphology.correct_scale(src_pos)
    target_pos = morphology.correct_scale(target_pos)

    return min(src_pos[3], target_pos[3])


def CreateProjection(morphconngraph, edge):
    '''Add a projection to the projections element based on the edge data'''

    project = net.Projection()


    edgedata = _GetEdgeData(morphconngraph, edge)

    type = edgedata['type']

    synapse_props = net.GlobalSynapticProperties()
    synapse_props.synapse_type = type.Name
    synapse_props.weight = _SynapseWeight(edgedata['source'], edgedata['target'])

    project.synapse_props.append(synapse_props)

#    print synapse_props.toxml()

    project.connections = net.Connections()

    project.name = "%d-%d" % (edge[0].ID, edge[1].ID)

    project.connections.append(CreateConnection(morphconngraph, edge))

    project.source_ = str(edge[0].ID)
    project.target_ = str(edge[1].ID)

    project.group = metaml.Group()

#    print project.toxml()

    return project


def CreateProjections(neuroml, morphconngraph):

    projections = net.Projections()
    projections.units = "Physiological Units"
    neuroml.projections = projections

    ed = list(morphconngraph.edges(data=True))

    for e in morphconngraph.edges(data=True):
        project = CreateProjection(morphconngraph, e)
        neuroml.projections.append(project)

    print projections.toxml()

    return projections


def ConnectivityToNeuroML(morphconngraph):
    '''Convert a connectivity graph to a neuroml file'''

    structList = []
    for n in morphconngraph.nodes():
        structList.append(n.ID)

    neuroml_elem = CreateDocument()

    neuroml_elem.populations = pyxb.BIND()
    neuroml_elem.cells = pyxb.BIND()
    neuroml_elem.projections = pyxb.BIND()

    neuroml_elem.populations = CreatePopulations(neuroml_elem, morphconngraph)
    neuroml_elem.projections = CreateProjections(neuroml_elem, morphconngraph)

    print "Building network from cell #'s " + str(structList)

    cellelems = []

    for cellid in structList:
        # morphgraph = self.ReadOrCreateVariable("morphology-%d" % cellid, self.CreateCleanedMorphGraph, StructureID=cellid)
        morphgraph = morphology.Load(cellid)

        cell_elem = MorphologyToCell(morphgraph)
        neuroml_elem.cells.append(cell_elem)

    return neuroml_elem


def ProcessQueue(graph, queue, processedNodes=None, segmentlist=None):
    '''Create an ml segment for the top node on the queue. 
       Then check all of the adjecent nodes to determine if 
       segments have been created.  If a segment has not been
       created then add that node the queue.  Continue until the
       queue is empty'''

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

    adjacentNodes = list(nx.all_neighbors(graph.graph, nx_node))

    SameCable = False
    if len(adjacentNodes) == 2:
        SameCable = True

    for node in adjacentNodes:

        if node.ID in processedNodes:
            continue

        cableid = ml_node.cable
        if not SameCable:
            cableid = _getnextcableid()

        mlChildNode = CreateSegment(node, parent=ml_node, cable=cableid)
        segmentlist.append(mlChildNode)

        queue.append((node, mlChildNode))

    return segmentlist


if __name__ == '__main__':
    pass