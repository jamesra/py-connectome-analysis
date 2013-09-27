'''
Created on May 27, 2013

@author: James Anderson
'''

import test.test_connectomics.test_model as test_model

import connectome_analysis.datamodels.graphs.morphologyconnectivity as morphconn
import connectome_analysis.datamodels.graphs.structurelocations as structlocgraph
import connectome_analysis.viewmodels.morphology as morphology
import connectome_analysis.views.neuromlview_18 as neuromlview_18
import connectome_analysis.views.neuromlview_20b1 as neuromlview_20b1
import os


class TestNeuroMLView(test_model.MorphologyGraphTest):
    '''
    classdocs
    '''

    cleanedmorphgraphpath = "morphologyGraph.pickle"

    @property
    def StructureID(self):
        return 476

    def CreateCleanedMorphGraph(self, StructureID):

        print "Downloading structure locations for %d" % StructureID
        structlocations = self.ReadOrCreateVariable("structlocations-%d" % StructureID, structlocgraph.Load, structureID=StructureID)

        print "Creating morphology graph"
        morphologyGraph = morphology.Morphology(structlocations)
        self.assertIsNotNone(morphologyGraph)

        print("Remove morpholgy subgraphs")
        morphologyGraph.RemoveBreaks()
        print("Remove morpholgy overlapping locations")
        morphologyGraph.RemoveOverlappingLocations()

        return morphologyGraph

    def test_CreateNeuroML20(self):

        morphologyGraph = self.ReadOrCreateVariable("morphology-%d" % self.StructureID, self.CreateCleanedMorphGraph, StructureID=self.StructureID)


        # print("Find largest radius node for use as soma")
        # node = morphologyGraph.LargestRadiusNode()
        # self.assertIsNotNone(node, "No node with largest radius returned")
        # self.assertGreater(node.Radius, 2600, "largest node has smaller radius than expected based on previous tests on structure 180")

        neuroml_xml = neuromlview_20b1.MorphologyToNeuroML(morphologyGraph)
        self.assertIsNotNone(neuroml_xml, "No neuroml v2.0 beta1 data returned")

        savefilepath = os.path.join(self.TestOutputPath, '%dv20b1.xml' % self.StructureID)
        print "Saving neuroml output to " + savefilepath
        with file(savefilepath, 'w') as f:
            f.write(neuroml_xml)

        self.assertTrue(os.path.exists(savefilepath))

    def test_CreateNeuroML18(self):

        morphologyGraph = self.ReadOrCreateVariable("morphology-%d" % self.StructureID, self.CreateCleanedMorphGraph, StructureID=self.StructureID)


        # print("Find largest radius node for use as soma")
        # node = morphologyGraph.LargestRadiusNode()
        # self.assertIsNotNone(node, "No node with largest radius returned")
        # self.assertGreater(node.Radius, 2600, "largest node has smaller radius than expected based on previous tests on structure 180")

        neuroml = neuromlview_18.MorphologyToNeuroML(morphologyGraph)
        neuroml_xml = neuroml.toxml()
        self.assertIsNotNone(neuroml_xml, "No neuroml v1.8 data returned")

        savefilepath = os.path.join(self.TestOutputPath, '%dv18.xml' % self.StructureID)
        print "Saving neuroml output to " + savefilepath
        with file(savefilepath, 'w') as f:
            f.write(neuroml_xml)

        self.assertTrue(os.path.exists(savefilepath))

    def test_CreateNeuroML18Network(self):


        rootcell = 8579  # Starburst AC

        morphconngraph = self.ReadOrCreateVariable("morphconn-%d" % rootcell, morphconn.Load, structureID=rootcell, hops=1)

        # A hack to add morphology graphs to the cache
        for n in morphconngraph.nodes():
            morphgraph = self.ReadOrCreateVariable("morphology-%d" % n.ID, self.CreateCleanedMorphGraph, StructureID=n.ID)
            morphology._morphologyCache[n.ID] = morphgraph

        neuroml_elem = neuromlview_18.ConnectivityToNeuroML(morphconngraph)
        self.assertIsNotNone(neuroml_elem, "No neuroml v1.8 element returned")

        neuroml_xml = neuroml_elem.toxml()
        self.assertIsNotNone(neuroml_xml, "No neuroml v1.8 data returned")
        self.assertGreater(len(neuroml_xml), 0, "No neuroml v1.8 data returned")

#        structList = []
#        for n in morphconngraph.nodes():
#            structList.append(n.ID)
#
#        print "Building network from cell #'s " + str(structList)
#
#        cellelems = []
#
#              cellelems.append(neuromlview_18.MorphologyToCell(morphgraph))
#
#        neuroml_xml = neuromlview_18.CreateDocument(cellelems)
#        self.assertIsNotNone(neuroml_xml, "No neuroml v1.8 data returned")

        savefilepath = os.path.join(self.TestOutputPath, '%dv18.xml' % rootcell)
        print "Saving neuroml output to " + savefilepath
        with file(savefilepath, 'w') as f:
            f.write(neuroml_xml)

        self.assertTrue(os.path.exists(savefilepath))
