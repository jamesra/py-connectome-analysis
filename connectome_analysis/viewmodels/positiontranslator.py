'''
Created on Jul 22, 2013

@author: u0490822
'''

import numpy as np
import scipy.spatial
import scipy.interpolate

from connectome_analysis.datamodels.graphs import structurelocations
from connectome_analysis.datamodels import queries
from connectome_analysis.viewmodels.morphology import Morphology

def XYZToArray(x, y, z):
    points = np.zeros((len(x.flat), 3))
    points[:, 0] = x.flat
    points[:, 1] = y.flat
    points[:, 2] = z.flat

    return points


def FetchStructurePoints(structs):
    '''Combines the points of all structures passed into a single list'''

    pointcollection = None
    for s in structs:

        print str(s.ID)
        locGraph = structurelocations.Load(s.ID)
        morphGraph = Morphology(locGraph)

        locData = morphGraph.Data

        if pointcollection is None:
            pointcollection = locData
        else:
            pointcollection = np.vstack((locData, pointcollection))

    return pointcollection


class ZNormalizer(object):
    '''
    Maps points Z-coordinate to a normalized depth relative to two surfaces.
    '''

    def __init__(self, TopSurfacePoints, BottomSurfacePoints):
        '''
        Constructor
        '''

        self.TopSurfacePoints = TopSurfacePoints
        self.BottomSurfacePoints = BottomSurfacePoints

        self.TopMapper = SurfaceMapper(self.TopSurfacePoints)
        self.BottomMapper = SurfaceMapper(self.BottomSurfacePoints)

    def Normalize(self, points):

        points = np.array(points, ndmin=2)

        topIntersect = self.TopMapper.VerticalIntersect(points)
        bottomIntersect = self.BottomMapper.VerticalIntersect(points)

        Thickness = topIntersect - bottomIntersect
        pointdepth = points[:, 2] - bottomIntersect

        normalizedDepth = pointdepth / Thickness

        return normalizedDepth



class SurfaceMapper():
    '''Creates a surface on the X,Y axes.  Given a point in X,Y returns the distance to the triangulation in Z'''

    def __init__(self, surfacepoints):

        self.points = surfacepoints

        self.tri = scipy.spatial.Delaunay(np.array(self.points[:, 0:2]))

        self.interpolator = scipy.interpolate.LinearNDInterpolator(self.tri, self.points[:, 2])

        self.rbfinterpolator = scipy.interpolate.Rbf(self.points[:, 0], self.points[:, 1], self.points[:, 2], smooth=5.0, function='thin_plate')


    def VerticalIntersect(self, points):
        '''Return the intersecting point on the surface along a line in Z'''

        z = self.rbfinterpolator(points[:, 0], points[:, 1])

        # new_z = z - points[:, 2]

#        iSimplex = self.tri.find_simplex(npPoints[:, 0:2])
#
#        self.tri.simplex()
#
#        interpolator = scipy.interpolate.LinearNDInterpolator(self.points[self.tri.simplex[iSimplex, 0:3]], points)

        # return new_z
        return z

    def SurfaceGrid(self, width, height):
        '''Returns height of surface at regular points along grid'''

        (minX, minY, maxX, maxY) = self.Bounds

        x_range = np.linspace(minX, maxX, width)
        y_range = np.linspace(minY, maxY, height)

        i_y, i_x = np.meshgrid(y_range, x_range, sparse=False, indexing='xy')

        z = self.rbfinterpolator(i_y, i_x)

        return XYZToArray(i_x, i_y, z)

    @property
    def Bounds(self):
        mapPoints = self.points;

        minX = np.min(mapPoints[:, 1]);
        maxX = np.max(mapPoints[:, 1]);
        minY = np.min(mapPoints[:, 0]);
        maxY = np.max(mapPoints[:, 0]);

        return (minX, minY, maxX, maxY);
