'''
Created on Oct 14, 2013

@author: u0490822
'''

import connectome_analysis.datamodels.graphs.morphologyconnectivity as morphconn
import connectome_analysis.datamodels.queries as queries
import connectome_analysis.viewmodels.distinctlabels as distinctlabels
import connectome_analysis.views.bookmarks as vb
import networkx
import os
import pickle
import glob
import numpy

PostSynapseTypeID = 35

class PickledQueries(object):
    '''Helper class copied from testbase.  Maintains on disk cache of queries for faster development iteration'''
    
    @property
    def classname(self):
        return str(self.__class__.__name__)

    @property
    def TestCachePath(self):
        '''Contains cached files from previous test runs, such as database query results.
           Entries in this cache should have a low probablility of changing and breaking tests'''
        if 'TESTOUTPUTPATH' in os.environ:
            TestOutputDir = os.environ["TESTOUTPUTPATH"]
            return os.path.join(TestOutputDir, "Cache", self.classname)
        else:
            self.fail("TESTOUTPUTPATH environment variable should specify test output directory")

        return None

    def ReadOrCreateVariable(self, varname, createfunc=None, *args, **kwargs):
        '''Reads variable from disk, call createfunc if it does not exist'''
        var = None
        if hasattr(self, varname):
            var = getattr(self, varname)
    
        if var is None:
            path = os.path.join(self.TestCachePath, varname + ".pickle")
            if os.path.exists(path):
                with open(path, 'r') as filehandle:
                    try:
                        var = pickle.load(filehandle)
                    except:
                        var = None
                        print("Unable to load graph from pickle file: " + path)
    
            if var is None and not createfunc is None:
                var = createfunc(*args, **kwargs)
                self.SaveVariable(var, path)
    
        return var

    def SaveVariable(self, var, path):
        fullpath = os.path.join(self.TestCachePath, path)

        if not os.path.exists(os.path.dirname(fullpath)):
            os.makedirs(os.path.dirname(fullpath))

        with open(fullpath, 'w') as filehandle:
            print("Saving: " + fullpath)
            pickle.dump(var, filehandle)


def LoadStructureIDs(path):
    '''Reads a text file where each line contains a unique structureID and returns a list of the IDs'''
    with open(path, 'r') as f:
        lines = f.readlines()

    IDs = []
    for line in lines:
        if line is None:
            continue

        line = line.strip()

        fixedLine = ""
        for c in line:
            if c.isdigit():
                fixedLine += c

        if len(fixedLine) == 0:
            continue

        IDs.append(int(fixedLine))

    return IDs


def StructureHeaderString(structure):
    '''Return a string for a structure in the form <ID> <Label>'''
    template = "%d %s"
    return template % (structure.ID, structure.Label)


def CellsByLabelString(LabelToStructures):
    '''Convert a dictionary keyed by strings and containing structures to a human readable form'''
    outstr = ""

    for L in LabelToStructures.keys():
        if L is None:
            outstr += "NoLabel\n"
        else:
            outstr += L + "\n"

        for s in LabelToStructures[L]:
            outstr += "\t" + StructureHeaderString(s) + "\n"

        outstr += "\n\n"

    return outstr


def _GetEdgeData(morphconngraph, edge):
    '''Helper function to fetch data for an edge.  Networkx does not return additional edge data for multi-directed graphs unless explicitely told to do so'''
    # If edge doesn't have three values it was probably fetched from networkx without using data=True
    if len(edge) < 3:
        val = morphconngraph.edges(edge, data=True)[0]
        return val[2]
    else:
        return edge[2]


def GetAllRadiiOfLocations(locations, scalar):
    return [loc.Radius * scalar for loc in locations]


def GetMaxRadiusOfLocations(locations, scalar, sectionThickness=90):
    maxRadius = max([loc.Radius * scalar for loc in locations])

    # Because the sections have a thickness, if a synapse is on two sections it must have some minimum thickness
    minPossibleRadius = len(locations) * (sectionThickness / 2.0)

    maxRadius = max(maxRadius, minPossibleRadius)

    return [maxRadius]


def GetCoordsOfMaxRadius(locations):
    indexofmax = numpy.argmax(numpy.double([loc.Radius for loc in locations]))

    location = locations[indexofmax]

    return numpy.double(location.VolumeX, location.VolumeY, location.Z)


def GetLocationWithMaxRadius(locations):
    indexofmax = numpy.argmax(numpy.double([loc.Radius for loc in locations]))

    return list(locations)[indexofmax]

#===============================================================================
#
# def GetCoordsOfLocations(locations):
#     maxRadius = max([loc.Radius * scalar for loc in locations])
#
#     # Because the sections have a thickness, if a synapse is on two sections it must have some minimum thickness
#     minPossibleRadius = len(locations) * (sectionThickness / 2.0)
#
#     maxRadius = max(maxRadius, minPossibleRadius)
#
#     return [maxRadius]
#===============================================================================


def GetEdgeLabelTuple(edge):
    '''Return the labels for cells connected by an edge in the graph'''
    sourceStruct = edge[0]
    targetStruct = edge[1]
    sourceLabel = distinctlabels.UniqueLabel(sourceStruct.Label)
    targetLabel = distinctlabels.UniqueLabel(targetStruct.Label)

    if sourceLabel is None:
        sourceLabel = "Unknown"
    if targetLabel is None:
        targetLabel = "Unknown"

    return (sourceLabel, targetLabel)

def GetAllPSDRadii(morphConnGraph, labelPattern, radiusFunction=None):
    '''Return the radius of all PSDs'''
    if radiusFunction is None:
        radiusFunction = GetAllRadiiOfLocations

    edges = list(morphConnGraph.edges(data=True))
    allPSDRadii = []
    for e in edges:
        edgedata = e[2]
        (sourceLabel, targetLabel) = GetEdgeLabelTuple(e)

        if not labelPattern in targetLabel:
            continue

        allPSDRadii.extend(radiusFunction(edgedata["target"], scalar=2.18))

    return allPSDRadii


def SourceInSet(edge, structIDs):
    return edge[0].ID in structIDs


def TargetInSet(edge, structIDs):
    return edge[1].ID in structIDs


def AddListToDict(dictOfLists, key, listvals):
    if not key in dictOfLists:
        dictOfLists[key] = listvals
    else:
        dictOfLists[key].extend(listvals)


def PSDRadiusByStructIDs(morphConnGraph, structIDs, radiusFunction=None):
    if radiusFunction is None:
        radiusFunction = GetAllRadiiOfLocations

    SourceLabelToRadius = {}
    TargetLabelToRadius = {}

    # for rod in RodStructures:
        # Fetch the rod's 7 structures

    edges = list(morphConnGraph.edges(data=True))

    for e in edges:
        edgedata = e[2]

        (sourceLabel, targetLabel) = GetEdgeLabelTuple(e)

        print edgedata["edgekey"] + " " + sourceLabel + " -> " + targetLabel

        if not (SourceInSet(e, structIDs) or TargetInSet(e, structIDs)):
            continue

        targetLocations = edgedata['target']
        if not targetLocations.structure.TypeID == PostSynapseTypeID:
            continue

        targetRadii = radiusFunction(edgedata["target"], scalar=2.18)

        if SourceInSet(e, structIDs):
            AddListToDict(SourceLabelToRadius, targetLabel, targetRadii)

        if TargetInSet(e, structIDs):
            AddListToDict(TargetLabelToRadius, sourceLabel, targetRadii)

    return (SourceLabelToRadius, TargetLabelToRadius)


def PSDRadiusByLabel(morphConnGraph, labelPattern, radiusFunction=None):
    '''Return the radius of child structures broken down by connection type'''

    if radiusFunction is None:
        radiusFunction = GetAllRadiiOfLocations

    SourceLabelToRadius = {}
    TargetLabelToRadius = {}

    # for rod in RodStructures:
        # Fetch the rod's 7 structures

    edges = list(morphConnGraph.edges(data=True))

    for e in edges:
        edgedata = e[2]

        (sourceLabel, targetLabel) = GetEdgeLabelTuple(e)

        print edgedata["edgekey"] + " " + sourceLabel + " -> " + targetLabel

        if not (labelPattern in sourceLabel or labelPattern in targetLabel):
            continue

        targetLocations = edgedata['target']
        if not targetLocations.structure.TypeID == PostSynapseTypeID:
            continue

        targetRadii = radiusFunction(edgedata["target"], scalar=2.18)

        if labelPattern in sourceLabel:
            AddListToDict(SourceLabelToRadius, targetLabel, targetRadii)

        if labelPattern in targetLabel:
            AddListToDict(TargetLabelToRadius, sourceLabel, targetRadii)

    return (SourceLabelToRadius, TargetLabelToRadius)


def DumpLabelToRadius(path, dictLabels):

    with open(path, 'w') as f:
        for L in dictLabels:

            valStr = L + "\t"
            for r in dictLabels[L]:
                valStr += '\t%g' % r

            f.write(valStr + '\n')

def LoadMotifs(path):

    MotifDict = {}
    motifFiles = glob.glob(os.path.join(path, "*.txt"))
    for filepath in motifFiles:
        IDs = LoadStructureIDs(filepath)

        basename = os.path.basename(filepath)
        (MotifName, ext) = os.path.splitext(basename)

        MotifDict[MotifName] = IDs

    return MotifDict


def GenerateBookmarks(morphConnGraph, structIDs):

    edges = list(morphConnGraph.edges(data=True))

    SourceToLocation = {}
    TargetToLocation = {}

    for e in edges:
        edgedata = e[2]

        (sourceLabel, targetLabel) = GetEdgeLabelTuple(e)

        print edgedata["edgekey"] + " " + sourceLabel + " -> " + targetLabel

        if not (SourceInSet(e, structIDs) or TargetInSet(e, structIDs)):
            continue

        targetLocations = edgedata['target']
        if not targetLocations.structure.TypeID == PostSynapseTypeID:
            continue

        loc = GetLocationWithMaxRadius(edgedata["target"])

        if SourceInSet(e, structIDs):
            AddListToDict(SourceToLocation, targetLabel, [loc])

        if TargetInSet(e, structIDs):
            AddListToDict(TargetToLocation, sourceLabel, [loc])

    OutputPartnerBookmarks = DictToBookmarkFolders("OutputPartnerPSDs", SourceToLocation)
    InputPartnerBookmarks = DictToBookmarkFolders("InputPartnerPSDs", TargetToLocation)

    return (InputPartnerBookmarks, OutputPartnerBookmarks)


def DictToBookmarkFolders(name, dictLocations):

    Folders = []
    for key in dictLocations.keys():
        folder = vb.CreateFolder(key, vb.BookmarksForLocations(dictLocations[key]))
        Folders.append(folder)

    return vb.CreateFolder(name, Folders)

if __name__ == '__main__':
    pickledData = PickledQueries()

    motifDict = LoadMotifs("motifs")

    # Build the structure cache
    # queries.GetStructures()

    structures = queries.GetStructuresOfType(1)  # pickledData.ReadOrCreateVariable("Structures", queries.GetStructuresOfType, 1)


    LabelToStructures = pickledData.ReadOrCreateVariable("LabelToStructures", distinctlabels.LabelsForStructures, structures)
    #LabelToStructures = distinctlabels.LabelsForStructures(structures)

    outstr = CellsByLabelString(LabelToStructures)

    with open("CellsByLabel.txt", 'w') as f:
        f.write(outstr)

    RodStructures = LabelToStructures["Rod BC"]

    rodIDs = [s.ID for s in RodStructures]

    motifDict["Rod"] = rodIDs

    allStructIDs = []  # s.ID for s in structures]
    for motif in motifDict.keys():
        allStructIDs.extend(motifDict[motif])

    allStructIDs.extend(rodIDs)
    allStructIDs.sort()

    # Fetch all of the rods and cells connected to the rods, use cached data if available
    # rodMorphConnGraph = pickledData.ReadOrCreateVariable("rodMorphConnGraph", morphconn.Load, rodIDs, hops=1)

    print("Building graph for all motif structures")
    motifMorphConnGraph = pickledData.ReadOrCreateVariable("allstructs_morphconn", morphconn.Load, allStructIDs, hops=1)



    BookmarkFolders = []

    for motif in motifDict.keys():
        print "Processing motif " + motif

        IDs = motifDict[motif]

        (InputPartnerBookmarks, OutputPartnerBookmarks) = GenerateBookmarks(motifMorphConnGraph, IDs)

        folder = vb.CreateFolder(motif, [InputPartnerBookmarks, OutputPartnerBookmarks])

        BookmarkFolders.append(folder)

        (SourceLabelToRadius, TargetLabelToRadius) = PSDRadiusByStructIDs(motifMorphConnGraph, IDs, radiusFunction=None)

        DumpLabelToRadius(motif + 'InputsPSDs.txt', TargetLabelToRadius)
        DumpLabelToRadius(motif + "OutputPartnerPSDs.txt", SourceLabelToRadius)

        (SourceLabelToRadius, TargetLabelToRadius) = PSDRadiusByStructIDs(motifMorphConnGraph, IDs, radiusFunction=GetMaxRadiusOfLocations)

        DumpLabelToRadius(motif + 'InputsPSDs_MaxRadiusOfPSD.txt', TargetLabelToRadius)
        DumpLabelToRadius(motif + "OutputPartnerPSDs_MaxRadiusOfPSD.txt", SourceLabelToRadius)

    AggregateFolder = vb.CreateFolder("Motifs", BookmarkFolders)

    xml = AggregateFolder.toxml()

    with open('Bookmarks.xml', 'w') as f:
        f.write(xml)
