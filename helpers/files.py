from helpers.types import is_number
import numpy
import sys
import re as regexp
import os
import csv
            

def load_into_matrix(fname,load_targets=True,num_targets=1,num_attributes=0,skip_first=True,input_delimiter=','):
    # source: http://stackoverflow.com/questions/4315506/load-csv-into-2d-matrix-with-numpy-for-plotting
    # the first row is a header

    if skip_first:
        matrix = numpy.loadtxt(open(fname,"rb"),delimiter=input_delimiter,skiprows=1)
    else:
        matrix = numpy.loadtxt(open(fname,"rb"),delimiter=input_delimiter,skiprows=0)
        
    if not load_targets:
        for target_index in numpy.arange(num_targets):
            for row in matrix:
                row[num_attributes+target_index] = None

    return matrix

def save_matrix_as_csv(location,matrix):
    if os.path.isfile(location):
        os.remove(location)
    numpy.savetxt(location,numpy.asarray(matrix),delimiter=',',fmt="%s")

def save_list_of_lists_as_csv(location,list_of_lists):
    if os.path.isfile(location):
        os.remove(location)

    with open(location, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(list_of_lists)

def save_list_as_csv(location,list):
    if os.path.isfile(location):
        os.remove(location) 
               
    with open(location, "wb") as f:
        writer = csv.writer(f)
        writer.writerow(list)

def get_partitions_dir_from_file_name(file_name):
    project_name = regexp.search('data/([^/]+)/[^/]+',file_name).group(1)

    return 'data/'+project_name+'/partitions'


def get_predictions_dir_from_partitions_dir(dirname):

    return dirname.replace('partitions','predictions')
