# File normalization and partioning utility

# normalizes and partitions the target file
# and then creates files containing training
# and test sets

# usage: ./preprocess_data <path_to_csv_file> 

import helpers.files as files
import helpers.prep as prep

from config.constants import *

import sys
import os
import numpy

if len(sys.argv) < 2:
    print ERROR+" Please provide the target CSV file containing the data.\n"
    sys.exit()

file_name = str(sys.argv[1])

#load everything into a matrix (not very scalable I think)
data_matrix = files.load_into_matrix(file_name,num_targets=NUM_TARGETS,num_attributes=NUM_ATTRS,input_delimiter=INPUT_DELIMITER,skip_first=HAS_HEADER)

#normalizing and shuffling
data_matrix = prep.normalize(data_matrix)
data_matrix = prep.shuffle(data_matrix)

#training set is twice as large as test set
train_set_matrix = prep.take_train_set(data_matrix)
test_set_matrix = prep.take_test_set(data_matrix)

# finding out the target directory where i should save the partitions

current_dir = os.path.dirname(os.path.realpath(__file__))

partitions_directory = files.get_partitions_dir_from_file_name(file_name)


#saving the preprocessed partitions

files.save_matrix_as_csv(partitions_directory+"/train_set.csv",train_set_matrix)
files.save_matrix_as_csv(partitions_directory+"/test_set.csv",test_set_matrix)

print SUCCESS+" Partitions successfully created\n"