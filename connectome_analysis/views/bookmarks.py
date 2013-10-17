'''
Created on Oct 17, 2013

@author: u0490822
'''

import vikingbookmarks.vikingbookmarks as vbm


def BookmarksForLocations(locations):

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

        bookmark.name = str(loc.ParentID)

        bookmarks.append(bookmark)

    return bookmarks;


def CreateFolder(name, elements):
    '''Create a bookmark folder containing the passed bookmark elements'''

    folder = vbm.Folder()

    folder.name = name

    for elem in elements:
        folder.append(elem)

    return folder


if __name__ == '__main__':
    pass