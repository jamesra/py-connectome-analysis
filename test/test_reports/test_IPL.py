'''
Created on Jul 22, 2013

@author: u0490822
'''
import unittest
import connectome_analysis.datamodels
import connectome_analysis.viewmodels
import numpy as np
from connectome_analysis.datamodels.graphs import structurelocations
from connectome_analysis.datamodels import queries

from connectome_analysis.viewmodels.morphology import Morphology, iLoc

import pyparsing
import matplotlib.pyplot as plt
from matplotlib import cm

from mpl_toolkits.mplot3d import Axes3D

import test.testbase
import os


import connectome_analysis.viewmodels.positiontranslator as position


class TestIPLDepth(test.testbase.TestBase):

    @property
    def IPLStructs(self):
        self._IPLStructs = self.ReadOrCreateVariable('_IPLStructs', queries.GetStructuresOfType, TypeID=224)
        return self._IPLStructs

    def FetchTypePoints(self, TypeID):
        IPLMarkerID = TypeID

        pointcollection = None

        structs = queries.GetStructuresOfType(TypeID)

        for s in structs:

            print str(s.ID)
            locGraph = structurelocations.Load(s.ID)
            morphGraph = Morphology(locGraph)

            locData = morphGraph.LocationArray

            if pointcollection is None:
                pointcollection = locData
            else:
                pointcollection = np.vstack((locData, pointcollection))

        return pointcollection

    def PlotBoundary(self, ax, points):

#        fig = plt.figure()
#        ax = fig.add_subplot(111, projection='3d')
#        ax.set_zlim(-33660, 0)
#        plt.show()


        # ax.scatter(xs=points[:, 0], ys=points[:, 1], zs=points[:, 2])
        ax.plot_trisurf(points[:, iLoc.iX], points[:, iLoc.iY], points[:, iLoc.iZ], cmap=cm.jet, shade=True)

        plt.xlabel('X')
        plt.ylabel('Y')
        ax.set_zlabel('Z')
        # self.AddLabels(ax, points)
        # ax.set_zlim(-33660 / 1000.0, 0 / 1000.0)


    def AddLabels(self, ax, points):

        LabeledIDs = []

        for s in self.IPLStructs:
            if s.ID in LabeledIDs:
                continue

            Label = s.Label

            locGraph = structurelocations.Load(s.ID)
            morphGraph = Morphology(locGraph)

            ax.text(x=morphGraph.LocationArray[0, iLoc.iX], y=morphGraph.LocationArray[0, iLoc.iY], z=morphGraph.LocationArray[0, iLoc.iZ], s=str(s.ID), label=Label)

    def CheckForDuplicates(self, points):

        numpoints = points.shape[0]

        sorted_index = np.argsort(points[:, 0])

        sorted_points = points[sorted_index, :]

        points = sorted_points

        for i in range(1, numpoints):

            if points[i, 0] + 1 >= points[i - 1, 0] and points[i, 0] - 1 <= points[i - 1, 0] :
                if points[i, 1] + 1 >= points[i - 1, 1] and points[i, 1] - 1 <= points[i - 1, 1] :
                    print str(points[i, :])



    def testIPL(self):

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        self.IPLBoundaryPoints = self.ReadOrCreateVariable('IPLBoundaryPoints', self.FetchTypePoints, TypeID=224)

       # self.CheckForDuplicates(self.IPLBoundaryPoints)
        self.SaveVariable(self.IPLBoundaryPoints, 'IPLBoundaryPoints.pickle')

        self.PlotBoundary(ax, self.IPLBoundaryPoints)

        self.GCLBoundaryPoints = self.ReadOrCreateVariable('GCLBoundaryPoints', self.FetchTypePoints, TypeID=235)
        self.SaveVariable(self.GCLBoundaryPoints, 'GCLBoundaryPoints.pickle')
        self.PlotBoundary(ax, self.GCLBoundaryPoints)

        TargetPath = os.path.join(self.TestOutputPath, "testIPL.svg")

        plt.savefig(TargetPath)

        # plt.show()

        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()