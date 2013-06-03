'''
Created on May 22, 2013

@author: James Anderson
'''

import os
import unittest


class TestBase(unittest.TestCase):
    '''
    classdocs
    '''

    @property
    def classname(self):
        return str(self.__class__.__name__)

    def setUp(self):
        '''
        Constructor
        '''
        super(TestBase, self).setUp()

        self.TestBaseDir = os.getcwd()

        self.OutputPath = os.path.join(os.getcwd(), "Test", "Data", "TestOutput", self.classname)
        if 'TESTDIR' in os.environ:
            self.TestBaseDir = os.environ["TESTDIR"]
            self.OutputPath = os.path.join(self.TestBaseDir, "TestOutput", self.classname)
