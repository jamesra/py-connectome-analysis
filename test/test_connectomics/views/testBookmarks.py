'''
Created on Oct 17, 2013

@author: u0490822
'''
import unittest
import os
import connectome_analysis.views.bookmarks as vb
import test.testbase


class dummyLoc(object):

    def __init__(self, X, Y, Z, Radius, ParentID=476):
        self.VolumeX = X
        self.VolumeY = Y
        self.Z = Z
        self.Radius = Radius
        self.ParentID = ParentID


class TestBookmarks(test.testbase.TestBase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.locations = []
        self.locations.append(dummyLoc(50000, 50000, 50, 50))
        self.locations.append(dummyLoc(60000, 50000, 51, 50))
        self.locations.append(dummyLoc(50000, 60000, 52, 50))

    def testCreateBookmark(self):
        bookmarks = vb.BookmarksForLocations(self.locations)

        folder = vb.CreateFolder("testCreateBookmarks", bookmarks)

        xml = folder.toxml()

        savefilepath = os.path.join(self.TestOutputPath, 'TestCreateBookmarks.xml')
        print "Saving bookmark output to " + savefilepath
        with file(savefilepath, 'w') as f:
            f.write(xml)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()