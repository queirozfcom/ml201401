from helpers.types import is_number
from config.constants import *
import numpy
import sys

def file_len(fname):
    num_headers = 0

    with open(fname) as f:
        for idx, line in enumerate(f):
            if is_header(line):
                num_headers += 1

    # starts at 0            
    return idx + 1 - num_headers

def is_header(line):
    for el in line.split(','):
        if is_number(el):
            return False

    return True

def num_attributes(fname):
    enough_lines = 10
    separator = ','
    #TODO check whether this works when file is < 10 lines long

    with open(fname) as f:
        for idx, line in enumerate(f):
            if idx == 0:
                num_attributes = len(line.split(separator))
            elif idx >= enough_lines:
                return num_attributes
            else:
                if len(line.split(separator)) != num_attributes:
                    print ERROR+" Not all lines have the same number of attributes in file "+fname+"\n"
                    sys.exit()
                

def load_into_matrix(fname):
    # source: http://stackoverflow.com/questions/4315506/load-csv-into-2d-matrix-with-numpy-for-plotting
    # the first row is a header
    return numpy.loadtxt(open(fname,"rb"),delimiter=",",skiprows=1)
