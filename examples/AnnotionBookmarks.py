'''
Created on Oct 30, 2013

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

import datetime

from operator import attrgetter



if __name__ == '__main__':
    locations = queries.LocationsByUsername('dmarshak')
    
#    oldLocs = []
    
#     for l in locations:
#         if l.LastModified <= datetime.date('2013-10-23'):
#             oldLocs.append(l)

    StructToLoc = vb.LocationsByParentStructure(locations)

    folders = []

    # StructIDs = [int(x) for x in StructToLoc.Keys()

    for k, locs in StructToLoc.items():
    
        

        locsSorted = sorted(locs, key=attrgetter('LastModified'), reverse=True)
        bookmarks = vb.BookmarksForLocations(locsSorted, 'LastModified')

        folder = vb.CreateFolder(str(k) + " " + str(locsSorted[0].LastModified), bookmarks)
        folders.append(folder)




    main = vb.CreateFolder("dmarshak", folders)

    with open('dmarshak.xml', 'w') as f:
        f.write(main.toxml())

    pass