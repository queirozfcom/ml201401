# this script calculates some metrics such as mean error and standard deviation for errors
# the arguments are as follows:
# - original test set (csv file)
# - test set with predictions calculated using some method
# - index of the column that was 'guessed' using an algorithm (0-based)

import helpers.files as files
import helpers.prep as prep

from config.constants import *

import os
import sys
import numpy


if len(sys.argv) != 4:
    print ERROR+""" Usage: \033[32mpython do_metrics.py <csv_file1> <csv_file2> <target_index>\033[0m
      This script can be used to compare two csv datasets. 
      It will calculate the mean difference in the given column for the two datasets.
    """
    sys.exit()

file_name1 = str(sys.argv[1])

if not os.path.isfile(file_name1):
    print ERROR+" File "+file_name1+" not found.\n"
    sys.exit()

file_name2 = str(sys.argv[2])

if not os.path.isfile(file_name2):
    print ERROR+" File "+file_name2+" not found.\n"
    sys.exit()

target_index = int(sys.argv[3])

set1 = numpy.loadtxt(open(file_name1,"rb"),delimiter=',',skiprows=0)
set2 = numpy.loadtxt(open(file_name2,"rb"),delimiter=',',skiprows=0)

assert len(set1)==len(set2),'I need both sets to have the same size.'

size = len(set1)

mean_error = 0.0

for i in range(size):
    row1 = set1[i]
    row2 = set2[i]

    mean_error += abs( row1[target_index] - row2[target_index] )

mean_error = round( mean_error/size, 5 )

print "\033[36mMEAN ERROR:\033[0m"+str(mean_error)