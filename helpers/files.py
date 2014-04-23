from helpers.types import is_number
from config.constants import *
import numpy
import sys
            

def load_into_matrix(fname):
    # source: http://stackoverflow.com/questions/4315506/load-csv-into-2d-matrix-with-numpy-for-plotting
    # the first row is a header
    return numpy.loadtxt(open(fname,"rb"),delimiter=DELIMITER,skiprows=1)
