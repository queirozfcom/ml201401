# Implementation of KNN algorithm with default K = 5
# This script expects a directory as argument.
# Given directory should have a file called train_set.csv and
# another file called test_set.csv

import helpers.files as files
import helpers.normalizers as normalizers
from config.constants import *
from string import replace
import csv
import numpy as np
import math
import random
import sys
import os
import time

if len(sys.argv) < 2:
    print ERROR+""" Please provide the directory where I can 
      find test and train partitions (they should be called "test_set.csv" and 
      "train_set".csv). Optionally, you can also set config options in config/
      constants.py\n"""
    sys.exit()

dir_name = sys.argv[1].lstrip('.').rstrip('/').strip(" ")

if not os.path.isfile(dir_name+'/train_set.csv'):
    print ERROR+" File "+dir_name+"/train_set.csv not found.\n"
    sys.exit()

if not os.path.isfile(dir_name+'/test_set.csv'):
    print ERROR+" File "+dir_name+"/test_set.csv not found.\n"
    sys.exit()

train_set_file = dir_name+'/train_set.csv'

train_set = files.load_into_matrix(train_set_file,skip_first=False)

# we won't load the targets because they're what we're trying to predict
prediction_set = files.load_into_matrix(dir_name+'/test_set.csv',skip_first=False,num_attributes=NUM_ATTRS,load_targets=False,num_targets=NUM_TARGETS)

indexes_to_use = filter(lambda x: False if x in EXCLUDE_ATTRS else True,np.arange(NUM_ATTRS))