import sys
import os
import numpy as np
import helpers.normalizers as norm

from config.constants import *

def normalize(matrix):

	if NORMALIZE_TARGETS:
		num_columns = NUM_ATTRS + NUM_TARGETS
	else:
		num_columns = NUM_ATTRS

	for col_no in range(num_columns):
		normalized_column = norm.normalize(matrix[:,col_no])
		for idx,row in enumerate(matrix):
			row[col_no]=normalized_column[idx]

	return matrix

def shuffle(matrix):
	np.random.shuffle(matrix)
	return matrix

def take_train_set(matrix):
	num_lines = len(matrix)
	size = int( TRAIN_RATIO * num_lines )

	return np.split(matrix,[size])[0]

def take_test_set(matrix):
	num_lines = len(matrix)
	size = int(TRAIN_RATIO * num_lines )

	return np.split(matrix,[size])[1]
