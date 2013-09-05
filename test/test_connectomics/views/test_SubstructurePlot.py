'''
Created on Jul 17, 2013

@author: u0490822
'''
import unittest
from connectome_analysis.views import plotsubstructures
import connectome_analysis.viewmodels.positiontranslator as position
import connectome_analysis.datamodels.queries as queries
import connectome_analysis.datamodels
import connectome_analysis.viewmodels.distinctlabels


import test.testbase


INL_IPL_MarkerTypeID = 224
IPL_GCL_MarkerTypeID = 235
GapJunctionTypeID = 28


def GroupByParent(substructures):

    parentStructs = {}
    for s in substructures:
        if not s.ParentID in parentStructs:
            parentStructs[s.ParentID] = [s]
        else:
            parentStructs[s.ParentID].append(s)

    return parentStructs


def GetLabelsForParentStructs(childstructs):

    print "Fetch unique labels for parent structs"
    ParentToSubstructures = GroupByParent(childstructs)

    ParentStructures = []

    for ID in ParentToSubstructures.keys():
        print ID
        if ID is None:
            continue

        s = connectome_analysis.datamodels.StructureCache[ID]
        ParentStructures.append(s)

    LabelToStructs = connectome_analysis.viewmodels.distinctlabels.LabelsForStructures(ParentStructures)
    return LabelToStructs


class TestSubstructurePlot(test.testbase.TestBase):

    @property
    def IPLStructs(self):
        self._IPLStructs = self.ReadOrCreateVariable('_IPLStructs', queries.GetStructuresOfType, TypeID=INL_IPL_MarkerTypeID)
        return self._IPLStructs

    @property
    def GCLStructs(self):
        self._GCLStructs = self.ReadOrCreateVariable('_GCLStructs', queries.GetStructuresOfType, TypeID=IPL_GCL_MarkerTypeID)
        return self._GCLStructs

    @property
    def IPLPoints(self):
        self._IPLPoints = self.ReadOrCreateVariable('_IPLPoints', position.FetchStructurePoints, structs=self.IPLStructs)
        return self._IPLPoints

    @property
    def GCLPoints(self):
        self._GCLPoints = self.ReadOrCreateVariable('_GCLPoints', position.FetchStructurePoints, structs=self.GCLStructs)
        return self._GCLPoints


    def testSubstructurePlot(self):

        positionTranslator = position.ZNormalizer(self.GCLPoints, self.IPLPoints)

        self.substructures = self.ReadOrCreateVariable('substructures', queries.GetStructuresOfType, TypeID=GapJunctionTypeID)

        LabelsForStructures = self.ReadOrCreateVariable('gapjunctions', GetLabelsForParentStructs, childstructs=self.substructures)

        substructureByParent = GroupByParent(self.substructures)

        plotsubstructures.PlotStructureByLabel(LabelsForStructures, substructureByParent, 28, positionTranslator)
        pass






if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()