import sys

def get_nearest_neighbours(row,matrix,indexes,num_neighbours=5,predict_target=0):

    neighbours_distance = list()

    for idx,other_row in enumerate(matrix):

        distance = get_distance(row,other_row,indexes)
        neighbours_distance.append([idx,distance])

    sorted_neighbours_distance = sorted(neighbours_distance, key=lambda neighbour: neighbour[1])

    return sorted_neighbours_distance[:num_neighbours]

def get_distance(row1,row2,attr_indexes):
    distance = 0.0

    for attribute_index in attr_indexes:
        attr_row1 = row1[attribute_index]
        attr_row2 = row2[attribute_index]
        
        distance += abs(attr_row2 - attr_row1)

    if distance == 0:
        # otherwise we'll get a division by zero
        return 0.01        
    else:
        return distance         
    