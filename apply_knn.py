# Implementation of KNN algorithm with default K = 5
# This script expects a directory as argument.
# Given directory should have a file called train_set.csv and
# another file called test_set.csv

import helpers.files as files
import helpers.normalizers as normalizers
import helpers.knn as knn

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

#all ok; let's move forward.

train_set_file = dir_name+'/train_set.csv'

train_set = files.load_into_matrix(train_set_file,skip_first=False)

# we won't load the targets because they're what we're trying to predict
prediction_set = files.load_into_matrix(dir_name+'/test_set.csv',skip_first=False,num_attributes=NUM_ATTRS,load_targets=False,num_targets=NUM_TARGETS)

#some attributes may be ignored if user has set config option EXCLUDE_ATTRS
indexes_to_use = filter(lambda x: False if x in EXCLUDE_ATTRS else True,np.arange(NUM_ATTRS))


for row in prediction_set:

    # start with zero
    prediction = 0.0 

    neighbour_index_distances_list = knn.get_nearest_neighbours(row,train_set,indexes_to_use,NUM_NEIGHBOURS,PREDICT_TARGET)
    
    total_weight = 0.0

    for neighbour_index_distance_pair in neighbour_index_distances_list:

        neighbour_index = neighbour_index_distance_pair[0]
        distance = neighbour_index_distance_pair[1]

        neighbour_target = train_set[neighbour_index][PREDICT_TARGET]

        weight = 1.0/distance

        total_weight += weight
        prediction += ( neighbour_target * weight )


    prediction = round(prediction/total_weight,NUM_DIGITS)

    row[PREDICT_TARGET] = prediction



predictions_dir_name = files.get_predictions_dir_from_partitions_dir(dir_name)


files.save_matrix_as_csv(predictions_dir_name+"_knn/prediction_set.csv",prediction_set)

print SUCCESS+" Predictions have been made using KNN algorithm.\n  Look at \033[36m"+predictions_dir_name+"_knn/prediction_set.csv\033[0m for the results\n"
