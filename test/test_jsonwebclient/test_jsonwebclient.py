'''
Created on May 16, 2013

@author: u0490822
'''
import unittest
import webclient.json.client as clients
from datetime import datetime


endpoint = "http://connectomes.utah.edu/Services/RC1/ConnectomeData.svc"

class Test(unittest.TestCase):


    def testRequestStructureTypes(self):
        client = clients.WCFDataServicesJSonClient(endpoint)

        structureTypesArray = client.Request('StructureTypes')
        self.assertGreaterEqual(len(structureTypesArray), 0, "No structure types returned from server")

    def testRequestStructure476(self):
        client = clients.WCFDataServicesJSonClient(endpoint)
        structures = client.Request('Structures(476L)')
        self.assertGreaterEqual(len(structures), 1, "No structure types returned from server")
        structure = structures[0]
        self.assertEqual(int(structure['ID']), 476)

    def testRequestStructureTypesAsObjects(self):
        client = clients.WCFDataServicesJsonObjectClient(endpoint)

        structureTypesArray = client.Request('StructureTypes')
        self.assertGreaterEqual(len(structureTypesArray), 0, "No structure types returned from server")

        for st in structureTypesArray:
            self.assertTrue(isinstance(st.ID, int), "ID should be an int type after object conversion")
            self.assertTrue(isinstance(st.Name, str), "Name should be an int type after object conversion")
            self.assertTrue(isinstance(st.Created, datetime), "Name should be an int type after object conversion")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()