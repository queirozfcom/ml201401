import sys
import os
import numpy as np
import helpers.normalizers as norm

def normalize(matrix):
	first_row = matrix[0,:]
	num_attributes = len(first_row)

	for attr_no in range(num_attributes):
		normalized_column = norm.normalize(matrix[:,attr_no])
		for idx,row in enumerate(matrix):
			row[attr_no]=normalized_column[idx]

	return matrix


def shuffle(matrix):
	np.random.shuffle(matrix)
	return matrix

def take_first_two_thirds(matrix):
	num_lines = len(matrix)
	two_thirds = int(2*(num_lines/3))

	return np.split(matrix,[two_thirds])[0]


def take_last_third(matrix):
	num_lines = len(matrix)
	two_thirds = int(2*(num_lines/3))

	return np.split(matrix,[two_thirds])[1]

def save_matrix_as_csv(location,matrix):
	if os.path.isfile(location):
		os.remove(location)
	np.savetxt(location,np.asarray(matrix),delimiter=',',fmt="%s")
