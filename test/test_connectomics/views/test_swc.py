'''
Created on May 27, 2013

@author: James Anderson
'''
import test.test_connectomics.test_model as test_model
import connectomics.viewmodel.morphology as morphology

import connectomics.view.swc as swc
import os


class TestSWCView(test_model.MorphologyGraphTest):
    '''
    classdocs
    '''
    @property
    def StructureID(self):
        return 6117

    def test_CreateSWC(self):

        morphologyGraph = morphology.Morphology(self.graph)
        self.assertIsNotNone(morphologyGraph)

        morphologyGraph.RemoveBreaks()
        morphologyGraph.RemoveOverlappingLocations()

        node = morphologyGraph.LargestRadiusNode()
        self.assertIsNotNone(node, "No node with largest radius returned")
        # self.assertGreater(node.Radius, 2600, "largest node has smaller radius than expected based on previous tests on structure 180")

        swcGraph = swc.MorphologyToSWC(morphologyGraph)
        self.assertIsNotNone(node, "No swc data returned")
        swcGraph.Save(os.path.join(self.OutputPath, '%d.swc' % self.StructureID))

        self.assertTrue(os.path.exists(os.path.join(self.OutputPath, '%d.swc' % self.StructureID)))
