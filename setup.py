'''
Created on Aug 30, 2013

@author: u0490822
'''


from ez_setup import use_setuptools
from setuptools import setup, find_packages

# This if test prevents an infinite recursion running tests from "python setup.py test"
if __name__ == '__main__':

    use_setuptools()

    packages = find_packages()

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

    install_requires = ["matplotlib",
                        "scipy",
                        "numpy",
                        "requests",
                        "pyxb>=1.2.2",
                        "PyGraphviz>=1.2",
                        "networkx>=1.8", ]

    setup(name='connectome_analysis',
          version='1.0',
          description="Access and visualization tools for connectome data",
          author="James Anderson",
          author_email="James.R.Anderson@utah.edu",
          url="https://github.com/jamesra/py-connectome-analysis",
          test_suite="test",
          install_requires=install_requires,
          packages=packages)
