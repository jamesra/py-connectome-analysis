'''
Created on Sep 5, 2013

@author: u0490822
'''

import sys
import os
import connectome_analysis.viewmodels.morphology as morphology
import connectome_analysis.views.swc as swc


def CreateSwc(structureID):
    morphologyGraph = morphology.Load(structureID)

    morphologyGraph.RemoveBreaks()
    morphologyGraph.RemoveOverlappingLocations()

    swcGraph = swc.MorphologyToSWC(morphologyGraph)
    swcGraph.Save(os.path.join(os.curdir, '%d.swc' % structureID))

    return swcGraph

if __name__ == '__main__':

    if len(sys.argv) > 1:
        for structIDStr in sys.argv[1:]:
            structID = int(structIDStr)
            print "Creating SWC for %d" % structID
            CreateSwc(structID)
    else:
        print "Missing structID parameters"
        print "ex: CreateSWC 180 476"