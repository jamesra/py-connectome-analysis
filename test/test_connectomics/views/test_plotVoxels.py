'''
Created on Feb 4, 2014

@author: u0490822
'''
import unittest
import os

import test.test_connectomics.test_model as test_model


import connectome_analysis.viewmodels.morphology as morphology
import connectome_analysis.views.plot as plot

class TestVoxelView(test_model.MorphologyGraphTest):

    @property
    def StructureID(self):
        '''override to change structureID for a test'''
        return 180

    @property
    def GraphName(self):
        return "Morphology"

    def CreateGraph(self, id):
        morphologyGraph = morphology.Load(id)
        morphologyGraph.RemoveBreaks()
        morphologyGraph.RemoveOverlappingLocations()

        return morphologyGraph

    def testVoxelVolumeCreation(self):

        morphologyGraph = self.ReadOrCreategraph()

        voxvol = plot.StructureToVoxelVolume(morphologyGraph)

        voxvol.Save(os.path.join("C:\\temp\\", '%d.binvox' % self.StructureID))
        voxvol.Save(os.path.join("C:\\temp\\", '%d.nrrd' % self.StructureID))

    def testLocationVoxelPlacement(self):

        Locations = morphology.M
#     def test BoundingBoxTest(self):
#
#


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()