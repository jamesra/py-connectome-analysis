'''
Created on Dec 30, 2013

@author: James Anderson

voxel converts geometric primitives to voxel representations.
'''
import os

import numpy as np
import nrrd
import binvox_rw


def _SaveNrrd(array, filepath):
    nrrd.write(filepath, array)


def _LoadNrrd(filepath):
    '''Returns data, options'''
    return nrrd.read(filepath)

def _SaveBinvox(vol, filepath):
    binvoxvol = binvox_rw.Voxels(vol.voxels, vol.voxels.shape, vol.origin, "%g %g %g" % (vol.voxsize[0], vol.voxsize[1], vol.voxsize[2]), 'xzy')
    binvox_rw.write(binvoxvol, filepath)

def VoxelRegion(boundingbox, vox_size, vox_origin=None):
    '''Returns the origin coordinates and number of voxels for a bounding box around each row of the boundingbox array'''

    ReshapeToOneDim = boundingbox.ndim == 1

    if ReshapeToOneDim:
        boundingbox = boundingbox.reshape(1, boundingbox.shape[0])

    if not vox_origin is None:
        boundingbox = boundingbox - np.tile(vox_origin, 2)

    vox_origin_remainder = boundingbox[:, 0:3] % vox_size

    vox_rounded = boundingbox[:, 0:3] - vox_origin_remainder

    # Round origin to nearest point on grid
    voxvol_origin = np.floor(vox_rounded / vox_size) * vox_size
    voxvol_max = np.ceil(boundingbox[:, 3:6] / vox_size) * vox_size

    # Calculate how many voxels in volume
    vox_count = (voxvol_max - voxvol_origin) / vox_size

    if ReshapeToOneDim:
        return (voxvol_origin.flatten(), vox_count.flatten())
    else:
        return (voxvol_origin, vox_count)

class Volume(object):
    '''A voxel volume'''

    @property
    def voxels(self):
        return self._voxels

    @property
    def voxparams(self):
        return self._voxparams

    @property
    def origin(self):
        return self.voxparams.origin

    @property
    def voxsize(self):
        return self.voxparams.voxsize

    @classmethod
    def Load(cls, filepath):
        if not os.path.exists(filepath):
            raise Exception("Volume.Load missing input file: " + filepath)

        (name, ext) = os.path.splitext(filepath)
        vol = Volume()

        if ext.lower() == '.nrrd':
            data, options = _LoadNrrd(filepath)
            vol._voxels = data
            assert(False)
            vol._voxparams = None
        else:
            raise Exception("Unexpected file extension when saving voxel volume: " + filepath)

    @classmethod
    def Create(cls, voxel_size, voxel_count, origin=None, dtype=None):
        vol = Volume()

        if origin is None:
            origin = np.array(0, 0)

        if dtype is None:
            dtype = np.int8

        vol._voxparams = VParams(origin=origin, voxel_size=voxel_size)

        vol._voxels = np.zeros(voxel_count, dtype=dtype)

        return vol

    def __init__(self):
        self._voxparams = None
        self._voxels = None

    def Save(self, filepath):
        (name, ext) = os.path.splitext(filepath)

        if ext.lower() == '.nrrd':
            _SaveNrrd(self.voxels, filepath)
        elif ext.lower() == '.binvox':
            _SaveBinvox(self, filepath)
        else:
            raise Exception("Unexpected file extension when saving voxel volume: " + filepath)

    def CoordToIndex(self, position):
        return self._voxparams.CoordToIndex(position)

    def IndexToCoord(self, index):
        scaledindex = index * self.voxsize
        scaledtranslatedindex = scaledindex + self.origin
        return scaledtranslatedindex


class VParams(object):
    '''Parameters for a voxelization.  Indicates origin of the voxel volume and the voxel dimensions'''

    @property
    def voxsize(self):
        '''Dimensions of a voxel, (height, width, depth)'''
        return self._voxsize

    @property
    def origin(self):
        '''Origin of the voxel volume'''
        return self._origin


    def __init__(self, origin, voxel_size):
        self._voxsize = np.array(voxel_size)
        self._origin = np.array(origin)


    def CoordToIndex(self, position):
        '''Return 3D voxel indicies for position'''
        adjustedpos = np.array(position) - self.origin
        index = np.floor(adjustedpos / self.voxsize)
        return index


def sphere(center, radius):
    '''Convert a sphere to a voxelization'''



if __name__ == '__main__':
    pass