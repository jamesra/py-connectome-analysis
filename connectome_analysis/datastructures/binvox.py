'''
Created on Feb 3, 2014

@author: u0490822
'''

def Write(array, filepath):

    with open(filepath, 'w') as fh:

        # Reorder the numpy array according to the binvox formats Y,X,Z ordering

        fh.writeline('#binvox 1')
        fh.writeline('dim %d %d %d' % (array.shape[0], array.shape[1], array.shape[2]))
        fh.writeline('translate %g %g %g' % (0, 0, 0))
        fh.writeline('scale 1')




if __name__ == '__main__':
    pass