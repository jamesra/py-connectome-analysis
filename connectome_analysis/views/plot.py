'''
Created on Jul 22, 2013

@author: u0490822
'''


# def plotsurface(points):

'''Plots points that represent surfaces, such as IPL Boundaries'''

import numpy as np

import rtree
from connectome_analysis.viewmodels.morphology import iLoc, iBBox, LocationsBoundingBox
import connectome_analysis.datastructures.voxel as voxel

import scipy.spatial.distance as sdist


def _GeneratorFunction(boundingboxes):
    '''Returns an iterator to walk the rows of a numpy array'''
    for i in range(0, boundingboxes.shape[0]):
        yield (int(boundingboxes[i, iBBox.ID]), boundingboxes[i, 0:6], int(boundingboxes[i, iBBox.ID]))


def _CreateSpatialIndex(iterfunc=None):
    p = rtree.index.Property()
    p.dimension = 3

    return rtree.index.Index(iterfunc, filename='3d_index', properties=p,)


def SpatialIndexFromMorphology(morphology):

    boundingBoxes = morphology.LocationBoundingBoxes
    idx = _CreateSpatialIndex(_GeneratorFunction(boundingBoxes))
    # idx.insert(boundingBoxes[:, iBBox.ID], boundingBoxes[:, 0:6], boundingBoxes[:, iBBox.ID])

    return idx


def _CreateVoxelVolume(boundingbox, vox_size):

    (voxvol_origin, vox_count) = voxel.VoxelRegion(boundingbox, vox_size)

    return voxel.Volume.Create(voxel_size=vox_size, voxel_count=vox_count, origin=voxvol_origin, dtype=np.uint8)


def AddBoundingBoxesToVolume(voxvol, BoundingBoxes):

        (RegionOrigin, RegionVoxCount) = voxel.VoxelRegion(BoundingBoxes, voxvol.voxsize, voxvol.origin)

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

def AddLocationSpheresToVolume(voxvol, Locations):
    BoundingBoxes = LocationsBoundingBox(Locations)[:, iBBox.MinX:iBBox.MaxZ + 1]

    (RegionOrigin, RegionVoxCount) = voxel.VoxelRegion(BoundingBoxes, voxvol.voxsize, voxvol.origin)
    indicies = RegionOrigin / voxvol.voxsize  # vol.CoordToIndex(RegionOrigin)
    endIndex = indicies + RegionVoxCount

    for iRow in range(0, Locations.shape[0]):
        AddSphereToVolume(voxvol, Locations[iRow, :], RegionOrigin=RegionOrigin[iRow, :], RegionVoxCount=RegionVoxCount[iRow, :])

def AddSphereToVolume(voxvol, Location, RegionOrigin, RegionVoxCount):
    sphere_center = np.array([Location[iLoc.X],
                             Location[iLoc.Y],
                             Location[iLoc.Z]])

    startingIndicies = (RegionOrigin / voxvol.voxsize)

    for iX in range(0, int(RegionVoxCount[0])):
        for iY in range(0, int(RegionVoxCount[1])):
            for iZ in range(0, int(RegionVoxCount[2])):

                indicies = startingIndicies + np.array([iX, iY, iZ])
                coord = voxvol.IndexToCoord(indicies)
                dist = sdist.pdist(np.vstack((sphere_center, coord)))
                voxvol.voxels[indicies[0], indicies[1], indicies[2]] |= dist <= Location[iLoc.Radius]

#                 if voxvol.voxels[indicies[0], indicies[1], indicies[2]]:
#                     print str(iX) + "," + str(iY) + "," + str(iZ)
#
#     print "\n"

def AddTaperedCylinderToVolume(voxvol, A, B):
    '''Fills voxels falling inside a tapered cylinder between locations A and B'''



def StructureToVoxelVolume(morphology):

    # idx = SpatialIndexFromMorphology(morphology)

    vox_size = np.array([0.5, 0.5, 0.09])

    voxvol = _CreateVoxelVolume(morphology.BoundingBox, vox_size)

    voxel_count = voxvol.voxels.shape

    # zIndicies = np.reshape(np.arange(0, voxel_count[2]), (voxel_count[2], 1))

    # (voxelOrigin, voxel_counts) = voxel.VoxelRegion(morphology.LocationBoundingBoxes, vox_size)

    # AddBoundingBoxesToVolume(voxvol, morphology.LocationBoundingBoxes[:, iBBox.MinX:iBBox.MaxZ + 1])

    AddLocationSpheresToVolume(voxvol, morphology.LocationArray)

#    for i in range(0, voxelBoxes.shape[0]):
        # continue

#
#
#     for iX in range(0, voxel_count[0]):
#         print "X: " + str(iX)
#         for iY in range(0, voxel_count[1]):
#
#             # Check if there are any hits on this X,Y column along Z, if not, skip
#             testStart = voxvol.IndexToCoord(np.array([iX, iY, 0]))
#             testEnd = voxvol.IndexToCoord(np.array([iX, iY, voxel_count[2]]))
#
#             columnbox = np.hstack((testStart, testEnd))
#             overlapping = list(idx.intersection(columnbox, objects=False))
#
#             if len(overlapping) == 0:
#                 continue
#
#             # print "Y: " + str(iY)
#             # testIndicies = np.hstack((np.ones((len(zIndicies), 1)) * iX,
#            #                         np.ones((len(zIndicies), 1)) * iY,
#             #                        zIndicies.copy()))
#
#             # voxel_positions = voxvol.IndexToCoord(testIndicies)
#             # overlapping = idx.intersection(voxel_positions)
#             for iZ in range(0, voxel_count[2]):
#                 voxel_position = voxvol.IndexToCoord(np.array([iX, iY, iZ]))
#                 voxel_position = np.tile(voxel_position, 2)
#                 overlapping = list(idx.intersection(voxel_position, objects=False))
#
#                 voxvol.voxels[iX, iY, iZ] = len(overlapping) > 0


    return voxvol




if __name__ == '__main__':
    pass