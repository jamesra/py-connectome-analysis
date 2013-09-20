'''
Created on May 22, 2013

@author: James Anderson
'''

import os
import unittest
import pickle
import logging


logging.basicConfig(level=logging.INFO)

class TestBase(unittest.TestCase):
    '''
    classdocs
    '''

    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(self.classname)
        super(TestBase, self).__init__(*args, **kwargs)

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

    @property
    def TestOutputPath(self):
        if 'TESTOUTPUTPATH' in os.environ:
            TestOutputDir = os.environ["TESTOUTPUTPATH"]
            return os.path.join(TestOutputDir, self.classname)
        else:
            self.fail("TESTOUTPUTPATH environment variable should specify test output directory")

        return None

    def setUp(self):
        '''
        Constructor
        '''
        super(TestBase, self).setUp()

        self.assertTrue('TESTOUTPUTPATH' in os.environ, "User's test environment must set TESTOUTPUTPATH environment variable to desired path for test output")

        if not os.path.exists(self.TestOutputPath):
            os.makedirs(self.TestOutputPath)

    def SaveVariable(self, var, path):
        fullpath = os.path.join(self.TestCachePath, path)

        if not os.path.exists(os.path.dirname(fullpath)):
            os.makedirs(os.path.dirname(fullpath))

        with open(fullpath, 'w') as filehandle:
            print("Saving: " + fullpath)
            pickle.dump(var, filehandle)

    def ReadOrCreateVariable(self, varname, createfunc=None, **kwargs):
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
                var = createfunc(**kwargs)
                self.SaveVariable(var, path)

        return var