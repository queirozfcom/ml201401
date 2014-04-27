# Implementation of KNN algorithm with default K = 5
# This script expects a directory as argument.
# Given directory should have a file called train_set.csv and
# another file called test_set.csv

import helpers.files as files
import helpers.normalizers as normalizers
import helpers.ann as ann
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

#some attributes may be ignored if user has set config option EXCLUDE_ATTRS
attributes_to_use = filter(lambda x: False if x in EXCLUDE_ATTRS else True,np.arange(NUM_ATTRS))


#training the network

#this is where the weights (between the input and the hidden layers) are kept
wij = ann.init_input_weights(len(attributes_to_use),NUM_NEURONS_HIDDEN_LAYER,NUM_DIGITS)

#these are the weights between the hidden layer and the output neuron (one per neuron in the hidden layer)
wj = ann.init_output_weights(NUM_NEURONS_HIDDEN_LAYER,NUM_DIGITS)

# i need as many input nodes as there are attributes so i'll just copy that
# note that this list may not be continuous in case an attribute is being ignored
x_values = list() 

# and as many yi's as there are hidden layer neurons
y_results = range(NUM_NEURONS_HIDDEN_LAYER) 
y_errors  = range(NUM_NEURONS_HIDDEN_LAYER)

y_network = None

for epoch in range(NUM_EPOCHS):
    for row in train_set:
        ############################
        # forward-feeding
        ############################
        x_values = ann.extract_attributes(row,attributes_to_use,NUM_DIGITS)

        for idx,y in enumerate(y_results):

            #weights used for current row, for the neuron whose index is idx
            weights_for_this_neuron = ann.extract_weights_for_neuron(wij,idx,NUM_DIGITS)
            
            # y is the output for this neuron
            y = ann.intermediate_output(x_values,weights_for_this_neuron,NUM_DIGITS)
            
            y_results[idx] = y
            
        y_network = ann.network_output(y_results,wj,NUM_DIGITS)    

        y_actual = ann.get_target_for_row(row,PREDICT_TARGET)

        ##########################
        # back-propagation
        ##########################
        network_error = y_actual - y_network

        #propagating the error to the hidden layer neurones
        for idx,y in enumerate(y_results):
            y_errors[idx] = network_error * wj[idx]

        #propagating the error to the weights between the input layer and the hidden layer
        for idx,y in enumerate(y_results):
            ann.update_incoming_weights_for_neuron(wij,x_values,idx, y_errors[idx],y_results[idx],LEARNING_RATE)
        
        #propagating the error to the weights between the hidden layer and the output node
        for idx,y in enumerate(y_results):
            ann.update_outgoing_weights_for_neuron(wj,idx,network_error,y_results,LEARNING_RATE)

for row in wij:
    ann.round_row(row,NUM_DIGITS)

ann.round_row(wj,NUM_DIGITS)

predictions_dir_name = files.get_predictions_dir_from_partitions_dir(dir_name)

files.save_list_of_lists_as_csv(predictions_dir_name+"_ann/trained_weights_for_input_nodes.csv",wij)
files.save_list_as_csv(predictions_dir_name+"_ann/trained_weights_for_output_node.csv",wj)

# running the test cases

for idx,row in enumerate(prediction_set):
    ann.run_instance(wij,wj,)

files.save_matrix_as_csv(predictions_dir_name+"_knn/prediction_set.csv",prediction_set)


print SUCCESS+""" Artificial Neural Network has been successfully trained.
  Look at \033[36m"""+predictions_dir_name+"""_ann/trained_weights_for_input_nodes.csv\033[0m and
  \033[36m"""+predictions_dir_name+"""_ann/trained_weights_for_output_node.csv\033[0m for the weights to be used.\n"""