'''
Created on Feb 4, 2014

@author: u0490822
'''


import sys
import os
import connectome_analysis.viewmodels.morphology as morphology
import connectome_analysis.views.plot as plot

def CreateBinVox(structureID):
    morphologyGraph = morphology.Load(structureID)

    morphologyGraph.RemoveBreaks()
    morphologyGraph.RemoveOverlappingLocations()

    voxvol = plot.StructureToVoxelVolume(morphologyGraph)

    voxvol.Save(os.path.join(os.curdir, '%d.binvox' % structureID))

    return voxvol


if __name__ == '__main__':

    if len(sys.argv) > 1:
        for structIDStr in sys.argv[1:]:
            structID = int(structIDStr)
            print "Creating SWC for %d" % structID
            CreateBinVox(structID)
    else:
        print "Missing structID parameters"
        print "ex: CreateSWC 180 476"