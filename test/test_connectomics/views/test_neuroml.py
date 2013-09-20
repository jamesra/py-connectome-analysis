'''
Created on May 27, 2013

@author: James Anderson
'''

import test.test_connectomics.test_model as test_model

import connectome_analysis.viewmodels.morphology as morphology
import connectome_analysis.views.neuromlview as neuromlview
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

    def test_CreateNeuroML(self):

        morphologyGraph = self.ReadOrCreateVariable("morphologyGraph", self.CreateCleanedMorphGraph)


        # print("Find largest radius node for use as soma")
        # node = morphologyGraph.LargestRadiusNode()
        # self.assertIsNotNone(node, "No node with largest radius returned")
        # self.assertGreater(node.Radius, 2600, "largest node has smaller radius than expected based on previous tests on structure 180")

        neuroml_xml = neuromlview.MorphologyToNeuroML(morphologyGraph)
        self.assertIsNotNone(neuroml_xml, "No neuroml data returned")

        savefilepath = os.path.join(self.TestOutputPath, '%d.xml' % self.StructureID)
        print "Saving neuroml output to " + savefilepath
        with file(savefilepath, 'w') as f:
            f.write(neuroml_xml)

        self.assertTrue(os.path.exists(savefilepath))
