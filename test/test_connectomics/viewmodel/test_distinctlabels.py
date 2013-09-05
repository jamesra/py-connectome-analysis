'''
Created on Jul 10, 2013

@author: u0490822
'''
import unittest
from connectome_analysis.viewmodels import distinctlabels

class Test(unittest.TestCase):


    def testName(self):


        sbyLabel = distinctlabels.LabelsForStructures()

        listLabels = list()
        for k in sbyLabel.keys():
            self.assertFalse(k in listLabels, "Duplicate label in Structures by label: " + str(k))
            listLabels.append(k)

            listStructs = sbyLabel[k]
            self.assertFalse(listStructs is None, "Structures by label has none structure list: " + str(k))
            self.assertFalse(len(listStructs) == 0, "Structures by label has zero length: " + str(k))

            print k + " : " + str(len(listStructs))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()