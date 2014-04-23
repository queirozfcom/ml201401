from helpers.types import is_number
from config.constants import *
import numpy
import sys
import re
            

def load_into_matrix(fname,load_targets=True):
    # source: http://stackoverflow.com/questions/4315506/load-csv-into-2d-matrix-with-numpy-for-plotting
    # the first row is a header

    matrix = numpy.loadtxt(open(fname,"rb"),delimiter=INPUT_DELIMITER,skiprows=1)

    if not load_targets:
        for target_index in numpy.arange(NUM_TARGETS):
            for row in matrix:
                row[NUM_ATTRS+target_index] = None

    return matrix


def get_partitions_dir(file_name):

    project_name = re.search('data/([^/]+)/[^/]+',file_name).group(1)

    return 'data/'+project_name+'/partitions'
