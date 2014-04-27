import sys
import os
import numpy as np
import helpers.normalizers as norm

def normalize(matrix,num_attrs,num_targets,normalize_targets=False):

	if normalize_targets:
		num_columns = num_attrs + num_targets
	else:
		num_columns = num_attrs

	for col_no in range(num_columns):
		normalized_column = norm.normalize(matrix[:,col_no])
		for idx,row in enumerate(matrix):
			row[col_no]=normalized_column[idx]

	return matrix

def shuffle(matrix):
	np.random.shuffle(matrix)
	return matrix

def take_train_set(matrix,train_ratio):
	num_lines = len(matrix)
	size = int( train_ratio * num_lines )

	return np.split(matrix,[size])[0]

def take_test_set(matrix,train_ratio):
	num_lines = len(matrix)
	size = int(train_ratio * num_lines )

	return np.split(matrix,[size])[1]
