'''
Created on Oct 17, 2013

@author: u0490822
'''

import vikingbookmarks.vikingbookmarks as vbm

from operator import attrgetter 

def BookmarksForLocations(locations, NameAttribute=None):
    '''NameAttribute indicates which attribute should be used for the name'''
    
    if NameAttribute is None:
        NameAttribute = "ParentID"

    bookmarks = []

    for loc in locations:
        bookmark = vbm.bookmark()

        pos = vbm.position()
        pos.X = loc.VolumeX
        pos.Y = loc.VolumeY
        pos.Z = loc.Z

        view = vbm.view()
        view.Downsample = 8.0


        bookmark.Position = pos
        bookmark.View = view
        bookmark.Comment = str(loc.ParentID)

        if not hasattr(loc, NameAttribute):
            print "Error, object missing name attribute " + str(loc)
            continue

        bookmark.name = str(getattr(loc, NameAttribute))

        bookmarks.append(bookmark)

    return bookmarks;


def CreateFolder(name, elements):
    '''Create a bookmark folder containing the passed bookmark elements'''

    folder = vbm.Folder()

    folder.name = name

    for elem in elements:
        folder.append(elem)

    return folder

#
# def dictToBookmarks(dictObjs):
#     '''Convert a dictionary to a list of bookmarks folders'''
#
#     for k, values in dictObjs:
#
#         bookmarks = []
#
#         for v in values:
#             if isinstance(v, Location)


def LocationsByParentStructure(locations):
    '''Return a dictionary keyed by structure ID containing locations for that structureID'''

    StructToLoc = {}

    for l in locations:
        if l.ParentID in StructToLoc:
            StructToLoc[l.ParentID].append(l)
        else:
            StructToLoc[l.ParentID] = [l]

    return StructToLoc


if __name__ == '__main__':
    pass