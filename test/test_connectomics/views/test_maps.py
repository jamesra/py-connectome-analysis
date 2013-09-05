'''
Created on Jun 19, 2013

@author: u0490822
'''
import unittest
import connectome_analysis.views.mappings as mappings


class LabelTest(unittest.TestCase):

    InputLabelList = [' GAC Aii ',
                      'Rod BC ',
                      ' Rod BC',
                      'CBa1w[G-, <> Aii]',
                      'CBa1w [G-] ',
                      'GAC Aii']

    OutputLabelList = ['GAC Aii',
                       'Rod BC',
                       'Rod BC',
                       'CBa1w',
                       'CBa1w',
                       'GAC Aii']

    OutputLabelTagsList = [[],
                       [],
                       [],
                       ['G-', '<> Aii'],
                       ['G-'],
                       []]


    def testLabels(self):

        for (iLabel, label ) in enumerate(LabelTest.InputLabelList):
            (labelbase, labeltags) = mappings.LabelParts(label)
            self.assertEqual(labelbase, LabelTest.OutputLabelList[iLabel], 'Unexpected output for label name from mappings.LabelParts')

            self.assertEqual(len(labeltags), len(LabelTest.OutputLabelTagsList[iLabel]), 'Incorrect number of tags returned')

            for (iTag, tag) in enumerate(labeltags):
                self.assertEqual(tag, LabelTest.OutputLabelTagsList[iLabel][iTag])


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()