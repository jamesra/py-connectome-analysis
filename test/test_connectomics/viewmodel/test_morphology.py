'''
Created on Feb 10, 2014

@author: u0490822
'''
import unittest
import numpy as np

import connectome_analysis.viewmodels.morphology as morph

class TestMorphology(unittest.TestCase):


    def testLoadMorphologyFromStructureID(self):

        morphgraph = morph.Load(180, useCache=True)
        self.assertIsNotNone(morphgraph, "No morphology graph for structure")

    def testLoadMorphologyFromArray(self):

        LocationArray = np.array([[1, 0, 0, 0, 5],
                                  [2, 0, 0, 1, 6],
                                  [3, 0, 0, 2, 3],
                                  [4, 0, 0, 3, 4]])

        morphgraphLocationArray = morph.Morphology.CreateFromLocationArray(LocationArray)
        self.assertIsNotNone(morphgraphLocationArray, "No morphology graph for structure")
        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()