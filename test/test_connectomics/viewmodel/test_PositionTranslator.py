'''
Created on Jul 24, 2013

@author: u0490822
'''
import unittest
import connectome_analysis.viewmodels.positiontranslator as position
import test.testbase
import connectome_analysis.datamodels.queries as queries


import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import os

INL_IPL_MarkerTypeID = 224
IPL_GCL_MarkerTypeID = 235


def InvalidIndicies(points):
    '''Removes rows with a NAN value and returns a list of indicies'''

    numPoints = points.shape[0]

    nanArray = np.isnan(points)

    nan1D = None
    if(len(nanArray.shape) > 1):
        nan1D = nanArray.any(axis=len(points.shape) - 1)
    else:
        nan1D = nanArray

    invalidIndicies = np.nonzero(nan1D)[0]
    points = np.delete(points, invalidIndicies, axis=0)

    assert(points.shape[0] + invalidIndicies.shape[0] == numPoints)

    return (points, invalidIndicies);

class TestPositionTranslator(test.testbase.TestBase):


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


    def testPositionTranslator(self):

        positionTranslator = position.ZNormalizer(self.GCLPoints, self.IPLPoints)

        translatedPoints = positionTranslator.Translate([100, 100, -15])
        z = translatedPoints[0, 2]
        self.assertTrue(z > 0 and z < 1, "Z not within range 0 to 1.0")

        bottom_points = positionTranslator.BottomMapper.SurfaceGrid(32, 32)
        top_points = positionTranslator.TopMapper.SurfaceGrid(32, 32)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d', aspect='equal')

        self.PlotBoundary(ax, bottom_points)
        self.PlotBoundary(ax, top_points)

        TargetPath = os.path.join(self.TestOutputPath, "testPositionTranslator.svg")

        plt.savefig(TargetPath)

        # plt.show()



    def testFlattenedGCL(self):

        positionTranslator = position.ZNormalizer(self.GCLPoints, self.IPLPoints)

        interpolator = position.SurfaceMapper(self.GCLPoints)

        points = positionTranslator.BottomMapper.SurfaceGrid(32, 32)


        # z = interpolator.VerticalIntersect(self.IPLPoints)
        z = interpolator.VerticalIntersect(points)

        (NonNanZ, invalidIndicies) = InvalidIndicies(z)

        NewIPLPoints = np.delete(points, invalidIndicies, axis=0)
        FlattenedIPLPoints = NewIPLPoints
        FlattenedIPLPoints[:, 2] = NonNanZ

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d', aspect='equal')

        self.PlotBoundary(ax, FlattenedIPLPoints)

        TargetPath = os.path.join(self.TestOutputPath, "testFlattenedGCL.svg")

        plt.savefig(TargetPath)

        # plt.show()

        pass



    def PlotBoundary(self, ax, points):

#        fig = plt.figure()
#        ax = fig.add_subplot(111, projection='3d')
#        ax.set_zlim(-33660, 0)
#        plt.show()


        # ax.scatter(xs=points[:, 0], ys=points[:, 1], zs=points[:, 2])
        ax.plot_trisurf(points[:, 0], points[:, 1], points[:, 2], cmap=cm.jet)

        plt.xlabel('X')
        plt.ylabel('Y')
        ax.set_zlabel('Z')
        # self.AddLabels(ax, points)
        # ax.set_zlim(-33660 / 1000.0, 0 / 1000.0)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()