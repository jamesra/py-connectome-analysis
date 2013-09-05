'''
Created on Aug 30, 2013

@author: u0490822
'''


from distutils.core import setup

try:
    print ""
    with open("readme_setup.txt", 'r') as f:
        lines = f.readlines()
        for l in lines:
            print l.rstrip()
    print ""
    print ""
except:
    print "Unable to print readme_setup.txt instructions"


setup(name='connectome_analysis',
      version='1.0',
      description="Access and visualization tools for connectome data",
      author="James Anderson",
      author_email="James.R.Anderson@utah.edu",
      url="https://github.com/jamesra/py-connectome-analysis",
      packages=["connectome_analysis",
                "connectome_analysis.datamodels",
                "connectome_analysis.datamodels.cache",
                "connectome_analysis.datamodels.graphs",
                "connectome_analysis.viewmodels",
                "connectome_analysis.views",
                "connectome_analysis.webclient",
                "connectome_analysis.webclient.json"])
