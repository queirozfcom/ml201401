def get_nearest_neighbours(row,train_matrix,num_neighbours=5):


def get_distance(row1,row2):
	# if they are the same, return a number close to zero but
	# not zero itself! otherwise we'll get a division by zero
	# when calculating the weights
	