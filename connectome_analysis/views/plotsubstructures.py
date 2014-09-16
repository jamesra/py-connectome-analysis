'''
Created on Jul 17, 2013

@author: u0490822
'''

import connectome_analysis.datamodels
from connectome_analysis.datamodels import StructureCache
from connectome_analysis.datamodels import StructurePositionCache
import  connectome_analysis.viewmodels.distinctlabels
import connectome_analysis.viewmodels.morphology
from connectome_analysis.viewmodels.substructurelocations import SubstructureLocations

from connectome_analysis.datamodels import queries

import matplotlib.pyplot as plt
import numpy as np
import os


def PlotStructureXYByLabel(LabelToStructs, substructureByParent, typeID, PositionTranslator=None, path=None, title=None):
    '''Puts all structures with a given type on a 2D plot'''

    Y = 0
    
    if not isinstance(typeID,list):
        typeID = [typeID]

    if not os.path.exists(path):
        os.makedirs(path)

    loopmax = 3
    iLoop = 0

    labelList = [];

    ySpread = 1.5

    colors = "bgrcmykw"
    icolor = 0

    StructurePositionCache.PopulateAll()

    labels = LabelToStructs.keys()
    labels.sort()
    labels.reverse()

    for label in labels:

        fig = plt.figure()
        plt.cla()
        axes = fig.gca()
        print label

        listStructs = LabelToStructs[label]
        
        if label is None:
            label = "No label"

        if '\\' in label:
            label = label.replace('\\', '-')

        if '<' in label:
            label = label.replace('<', '-')

        if '>' in label:
            label = label.replace('>', '-')

        if '/' in label:
            label = label.replace('/', '-')


        positionList = []
        colorlist = []
        for s in listStructs:
            substructures = substructureByParent[s.ID]

            for sub in substructures:
                if not sub.TypeID in typeID:
                    continue

                icolor = sub.TypeID % len(colors)
                colorlist.append(colors[icolor])
                pos = connectome_analysis.datamodels.StructurePositionCache[sub.ID]
                positionList.append(pos)

        if len(positionList) == 0:
            continue

        labelList.append(label)

        numPositions = len(positionList)

        if numPositions <= 1:
            continue

        locPosition = np.zeros(shape=(numPositions, 3))
        points = np.zeros(shape=(numPositions, 2))

        for i, childPosition in enumerate(positionList):
            locPosition[i, :] = np.array([childPosition.X, childPosition.Y, childPosition.Z])



        locPosition = connectome_analysis.viewmodels.morphology.correct_scale(locPosition)

        locPosition[:, 2] = 0
#        i = 0
        # randValues = ((np.random.random(numPositions) * ySpread * 2) - ySpread) + Y
        # locPosition[:, 1] = randValues

        Y = Y + 5

        axes.scatter(x=locPosition[:, 0], y=locPosition[:, 1], marker="+", axes=axes, c=colorlist)

#         icolor += 1
#         if icolor >= len(colors):
#             icolor = 0

#        iLoop += 1
#        if iLoop > loopmax:
#            break

#         plt.yticks(np.arange(len(labelList)) * 5, labelList)
        plt.xlim((np.min(locPosition[:, 0]) - 5, np.max(locPosition[:, 0]) + 5))
        plt.ylim((np.min(locPosition[:, 1]) - 5, np.max(locPosition[:, 1]) + 5))
#         plt.ylim((-ySpread, (len(labelList) * 5) + ySpread))
#         plt.xlabel("Z Depth 0 to 1.0")
#         plt.ylabel("Cell label")
        plt.title(title + " " + label + " in RC1")

        if path is None:
            plt.show()
        else:
            plt.savefig(os.path.join(path, label + '.svg'), dpi=300)


def PlotStructureByLabel(LabelToStructs, substructureByParent, typeID, PositionTranslator=None, path=None, title=None):
    '''Puts all structures with a given type on a 2D plot'''
    if not isinstance(typeID, list):
        typeID = [typeID]

    fig = plt.figure()
    axes = fig.gca()
    Y = 0

    loopmax = 3
    iLoop = 0

    labelList = [];

    ySpread = 1.5

    colors = "bgrcmykw"
    icolor = 0

    StructurePositionCache.PopulateAll()

    labels = LabelToStructs.keys()
    labels.sort()
    labels.reverse()

    for label in labels:


        print label

        listStructs = LabelToStructs[label]

        if label is None:
            label = "No label"

        if '\\' in label:
            label.replace('\\', '-')

        if '/' in label:
            label.replace('/', '-')


        positionList = []
        for s in listStructs:
            substructures = substructureByParent[s.ID]

            for sub in substructures:
                if not sub.TypeID in typeID:
                    continue

                pos = connectome_analysis.datamodels.StructurePositionCache[sub.ID]
                positionList.append(pos)

        if len(positionList) == 0:
            continue

        labelList.append(label)

        numPositions = len(positionList)

        locPosition = np.zeros(shape=(numPositions, 3))
        points = np.zeros(shape=(numPositions, 2))

        for i, childPosition in enumerate(positionList):
            locPosition[i, :] = np.array([childPosition.X, childPosition.Y, childPosition.Z])

        locPosition = connectome_analysis.viewmodels.morphology.correct_scale(locPosition)

        if not PositionTranslator is None:
            locPosition = PositionTranslator.Translate(locPosition)

        i = 0
        randValues = ((np.random.random(numPositions) * ySpread * 2) - ySpread) + Y
        locPosition[:, 1] = randValues

        Y = Y + 5

        axes.scatter(x=locPosition[:, 2], y=locPosition[:, 1], marker="+", axes=axes, c=colors[icolor])

        icolor += 1
        if icolor >= len(colors):
            icolor = 0

#        iLoop += 1
#        if iLoop > loopmax:
#            break

    plt.yticks(np.arange(len(labelList)) * 5, labelList)
    plt.xlim((0, 1))
    plt.ylim((-ySpread, (len(labelList) * 5) + ySpread))
    plt.xlabel("Z Depth 0 to 1.0")
    plt.ylabel("Cell label")
    plt.title(title)

    if path is None:
        plt.show()
    else:
        plt.savefig(path, dpi=300)
