'''
Created on Aug 30, 2013

@author: u0490822
'''


from distutils.core import setup

print ""
print "Connectome_analysis uses the following third-party packages which must be installed"
print "  numpy"
print "  scipy"
print "  networkx"
print "  requests"
print "  matplotlib"
print ""


setup(name='connectome_analysis',
      version='1.0',
      description="Access and visualization tools for connectomes.  Connectome data access for data hosted via ODATA.",
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
