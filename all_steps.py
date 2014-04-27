# this script runs preprocess_data.py and
# apply_knn.py having as parameter a single .csv
# file. This was created in order to make it easier
# to run this sequence multiple times.

import helpers.files as files
import helpers.prep as prep

from config.constants import *

import sys
import os

if len(sys.argv) < 2:
    print ERROR+" Please provide the target CSV file containing the data.\n"
    sys.exit()

if not os.path.isfile(sys.argv[1]):
    print ERROR+" File "+str(sys.argv[1])+" not found.\n"
    sys.exit()

file_name = str(sys.argv[1])

os.system("python preprocess_data.py "+file_name)

partitions_directory_name = files.get_partitions_dir_from_file_name(file_name)

os.system("python apply_knn.py "+ partitions_directory_name)