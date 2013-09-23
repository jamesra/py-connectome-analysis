'''
Created on May 27, 2013

@author: James Anderson
'''

import test.test_connectomics.test_model as test_model

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

    def CreateCleanedMorphGraph(self):

        print "Creating morphology graph"
        morphologyGraph = morphology.Morphology(self.graph)
        self.assertIsNotNone(morphologyGraph)

        print("Remove morpholgy subgraphs")
        morphologyGraph.RemoveBreaks()
        print("Remove morpholgy overlapping locations")
        morphologyGraph.RemoveOverlappingLocations()

        return morphologyGraph

    def test_CreateNeuroML20(self):

        morphologyGraph = self.ReadOrCreateVariable("morphologyGraph", self.CreateCleanedMorphGraph)


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

        morphologyGraph = self.ReadOrCreateVariable("morphologyGraph", self.CreateCleanedMorphGraph)


        # print("Find largest radius node for use as soma")
        # node = morphologyGraph.LargestRadiusNode()
        # self.assertIsNotNone(node, "No node with largest radius returned")
        # self.assertGreater(node.Radius, 2600, "largest node has smaller radius than expected based on previous tests on structure 180")

        neuroml_xml = neuromlview_18.MorphologyToNeuroML(morphologyGraph)
        self.assertIsNotNone(neuroml_xml, "No neuroml v1.8 data returned")

        savefilepath = os.path.join(self.TestOutputPath, '%dv18.xml' % self.StructureID)
        print "Saving neuroml output to " + savefilepath
        with file(savefilepath, 'w') as f:
            f.write(neuroml_xml)

        self.assertTrue(os.path.exists(savefilepath))

    def test_CreateNeuroML18Network(self):

        rootcell = 180


        morphologyGraph = self.ReadOrCreateVariable("morphologyGraph", self.CreateCleanedMorphGraph)


        # print("Find largest radius node for use as soma")
        # node = morphologyGraph.LargestRadiusNode()
        # self.assertIsNotNone(node, "No node with largest radius returned")
        # self.assertGreater(node.Radius, 2600, "largest node has smaller radius than expected based on previous tests on structure 180")

        neuroml_xml = neuromlview_18.MorphologyToNeuroML(morphologyGraph)
        self.assertIsNotNone(neuroml_xml, "No neuroml v1.8 data returned")

        savefilepath = os.path.join(self.TestOutputPath, '%dv18.xml' % self.StructureID)
        print "Saving neuroml output to " + savefilepath
        with file(savefilepath, 'w') as f:
            f.write(neuroml_xml)

        self.assertTrue(os.path.exists(savefilepath))
