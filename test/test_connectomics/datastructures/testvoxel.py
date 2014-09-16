'''
Created on Feb 3, 2014

@author: u0490822
'''
import unittest
import numpy as np
import connectome_analysis as ca
import connectome_analysis.datastructures.voxel as voxel

import scipy.spatial.distance as sdist


class VoxelTest(unittest.TestCase):

    def checkIndicies(self, vol, position, expectedIndicies, msg=None):

        indicies = vol.CoordToIndex(position)
        outstr = "Position %s should map to indicies of %s not %s" % (str(position), str(indicies), str(expectedIndicies))
        if not msg is None:
            outstr = outstr + "\n" + msg

        self.assertTrue(np.all(indicies == expectedIndicies), outstr)
        return


    def testCoordinates(self):

        vox_size = np.array([10, 10, 10.0])
        vol_dim = np.array([8, 16, 32])
        vol_origin = np.array([15, 0.0, 10.0])

        vol = ca.voxel.Volume.Create(voxel_size=vox_size, voxel_count=vol_dim, origin=vol_origin)

        indicies = vol.CoordToIndex(vol_origin)

        self.checkIndicies(vol, vol_origin, np.array([0, 0, 0]), "Origin should map to zero indicies")
        self.checkIndicies(vol, vol_origin - (vox_size / 2.0), np.array([-1, -1, -1]))
        self.checkIndicies(vol, vol_origin + (vox_size / 2.0), np.array([0, 0, 0]))
        self.checkIndicies(vol, vol_origin + vox_size, np.array([1, 1, 1]))
        self.checkIndicies(vol, vol_origin + (vox_size * 1.5), np.array([1, 1, 1]))

        vol.voxels[0:2, 0:4, 0:8] = True
        vol.Save('C:\\Temp\\TestVoxels.nrrd')
        vol.Save('C:\\Temp\\TestVoxels.binvox')

        pass


    def testSphere(self):
        '''Create a voxellized sphere to ensure our voxel pipeline works'''

        vox_size = np.array([1, 1, 1])
        vol_dim = np.array([32, 32, 32])
        vol_origin = np.array([0, 0.0, 0.0])

        sphere_center = (vol_dim / 2.0) * vox_size

        vol = ca.voxel.Volume.Create(voxel_size=vox_size, voxel_count=vol_dim, origin=vol_origin)

        for iX in range(0, vol_dim[0]):
            print "X: " + str(iX)
            for iY in range(0, vol_dim[1]):
                for iZ in range(0, vol_dim[2]):

                    coord = np.array([iX, iY, iZ])

                    dist = sdist.pdist(np.vstack((sphere_center, coord)))
                    vol.voxels[iX, iY, iZ] = np.any(dist < 12.0)

        vol.Save('C:\\Temp\\TestSphere.binvox')

    def AddBoundingBoxToVolume(self, voxvol, BoundingBox):

        (RegionOrigin, RegionVoxCount) = voxel.VoxelRegion(BoundingBox, voxvol.voxsize, voxvol.origin)

        indicies = RegionOrigin / voxvol.voxsize  # vol.CoordToIndex(RegionOrigin)

        endIndex = indicies + RegionVoxCount

        if indicies.ndim == 1:
            voxvol.voxels[indicies[0]:endIndex[0],
                          indicies[1]:endIndex[1],
                          indicies[2]:endIndex[2]] = True
        else:
            for iRow in range(0, indicies.shape[0]):
                voxvol.voxels[indicies[iRow, 0]:endIndex[iRow, 0],
                              indicies[iRow, 1]:endIndex[iRow, 1],
                              indicies[iRow, 2]:endIndex[iRow, 2]] = True


    def testBoundingBox(self):

        vox_size = np.array([10, 10, 10.0])
        vol_dim = np.array([32, 32, 32])
        vol_origin = np.array([0, 0.0, 0.0])

        BoundingBox = np.array([10, 19, 31, 19, 40, 50])

        (RegionOrigin, RegionVoxCount) = voxel.VoxelRegion(BoundingBox, vox_size)

        self.assertTrue(np.all(RegionOrigin == np.array([10, 10, 30])))
        self.assertTrue(np.all(RegionVoxCount == np.array([1, 3, 2])))

    def testBoundingBox2(self):
        '''Ensure all voxels within a bounding box are reported'''

        vox_size = np.array([10, 10, 10])
        vol_dim = np.array([32, 32, 32])
        vol_origin = np.array([15, 0.0, -10.0])

        vol = voxel.Volume.Create(voxel_size=vox_size, voxel_count=vol_dim, origin=vol_origin)

        # BoundingBox = [MinX MinY MinZ MaxX MaxY MaxZ]
        BoundingBox = np.array([27, 20, 1, 49, 40, 19])
        # BoundingBox = np.array([25, 20, -10, 55, 80, 30])

        self.AddBoundingBoxToVolume(vol, BoundingBox)

        BoundingBoxes = np.array([[75, 50, 30, 95, 80, 40],
                                  [75, 50, 50, 95, 120, 90]])

        self.AddBoundingBoxToVolume(vol, BoundingBoxes)

        vol.Save('C:\\Temp\\TestBoundingBox.binvox')

    def testBigVolume(self):
        '''Ensure all voxels within a bounding box are reported'''

        vox_size = np.array([.5, 1, 2])
        vol_dim = np.array([512, 512, 512])
        vol_origin = np.array([0, 0.0, 0])

        vol = voxel.Volume.Create(voxel_size=vox_size, voxel_count=vol_dim, origin=vol_origin)

        # BoundingBox = [MinX MinY MinZ MaxX MaxY MaxZ]
        BoundingBox = np.array([64, 1, 255, 255, 511, 356])
        # BoundingBox = np.array([25, 20, -10, 55, 80, 30])

        self.AddBoundingBoxToVolume(vol, BoundingBox)

        # BoundingBoxes = np.array([[75, 50, 30, 95, 80, 40],
        #                          [75, 50, 50, 95, 120, 90]])

        # self.AddBoundingBoxToVolume(vol, BoundingBoxes)

        vol.Save('C:\\Temp\\TestLargeVolume.binvox')




if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()