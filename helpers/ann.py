import random
import math
import sys

LOWER_BOUND = -0.5
UPPER_BOUND = 0.5

def init_input_weights(num_attrs,num_neurons,precision):
    l = list()
    for num in xrange(num_attrs):
        l_neurons = list()
        for neuron in xrange(num_neurons):
            l_neurons.append( round(random.uniform(LOWER_BOUND,UPPER_BOUND),precision) )
        
        l.append(l_neurons)        

    return l


def init_output_weights(num_neurons,precision):
    l = list()

    for num in xrange(num_neurons):
        l.append( round(random.uniform(LOWER_BOUND,UPPER_BOUND),precision) )

    return l


def extract_attributes(row,attribute_indexes_to_use,precision):
    l = list()

    for attr_index in attribute_indexes_to_use:
        l.append( round(row[attr_index],precision) )

    return l


def extract_weights_for_neuron(weights_matrix,neuron_index,precision):
    l = list()
    for row in weights_matrix:
        for idx,el in enumerate(row):
            if idx == neuron_index:
                l.append(el)

    return l


def sigmoid(x):
    val = 1 / (1+math.exp(-x))
    return round(val,10)#so we don't overflow


def intermediate_output(attribute_values,weights,precision):
    assert len(attribute_values) == len(weights), 'This is a dot (internal) product so these need to match'
    
    return round( dot_product(attribute_values,weights), precision )


def network_output(intermediate_ys,output_weights,precision):
    assert len(intermediate_ys)==len(output_weights),'This is a dot (internal) product so these need to match'

    return round( dot_product(intermediate_ys,output_weights), precision )


def get_target_for_row(row,target_index):
    return row[target_index]

#this updates the weights for all inputs connected to this neuron
#for example, if there's 4 inputs connected to a hidden neuron, then
#this function will update the 4 weights connecting them.
def update_incoming_weights_for_neuron(weights_matrix,attribute_values,neuron_index,neuron_error,current_neuron_y,learning_rate):

    weighted_sum = 0.0

    # the derivative of sigmoid function needs to be evaluated given the original signal (before 
    # the activation function was calculated
    for attribute_index,row in enumerate(weights_matrix):
        for target_neuron_index,weight in enumerate(row):
            if target_neuron_index == neuron_index:
                weighted_sum += ( weights_matrix[attribute_index][neuron_index] * attribute_values[attribute_index] )


    for attribute_index,row in enumerate(weights_matrix):

        #these are the weights that connect each input to this neuron (represented by neuron_index)
        for target_neuron_index,weight in enumerate(row):
            if target_neuron_index == neuron_index:
                old_weight = weights_matrix[attribute_index][neuron_index]

                # see http://en.wikipedia.org/wiki/Backpropagation#Derivation
                delta_weight = learning_rate * neuron_error * derivative_of_sigmoid(weighted_sum) * attribute_values[attribute_index]

                new_weight = old_weight + delta_weight

                weights_matrix[attribute_index][neuron_index] = new_weight


def update_outgoing_weights_for_neuron(weights_list,neuron_index, network_error, y_results ,learning_rate):
    assert len(weights_list) == len(y_results),' Since these are the weights connecting the hidden layer to the output node, these numbers should match. '

    weighted_sum = dot_product(weights_list,y_results)

    for idx,weight in enumerate(weights_list):
        if idx == neuron_index:
            old_weight = weight

            delta_weight = learning_rate * network_error * derivative_of_sigmoid(weighted_sum) * y_results[neuron_index]

            new_weight = old_weight + delta_weight

            weights_list[neuron_index] = new_weight

def dot_product(list1,list2):
    assert len(list1) == len(list2),' How can I possibly do dot product otherwise?'

    size = len(list1)

    product = 0.0

    for idx in range(size):
        product += ( list1[idx] * list2[idx] )

    return product

def derivative_of_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))

def round_row(row,precision):
    for idx in range(len(row)):
        row[idx] = round( row[idx],precision )

# runs a test instance (row) with given input and output weights
# and returns the prediction for target_value.
def run_test_instance(input_weights,output_weights,row,target_value,num_neurons,precision):

    for w_row in input_weights:
        assert num_neurons == len(w_row),'Each attribute much have one weight for each neuron in the hidden layer.'

    assert len(output_weights) == num_neurons,'There should be one output weight for each hidden-layer neuron.'

    neuron_intermediate_products = range(num_neurons)

    for attr_idx,weight_row in enumerate(input_weights):
        for neuron_idx,weight in enumerate(weight_row):
            value = row[attr_idx] * input_weights[attr_idx][neuron_idx]
            neuron_intermediate_products[neuron_idx] += value

    #we've calculated the values in each hidden-layer neuron
    #now we join them up using the output weights and work out
    #the final value which is the estimate for the given row.

    output = 0.0

    for neuron_idx,intermediate_value in enumerate(neuron_intermediate_products):
        output += intermediate_value * output_weights[neuron_idx]

    return round( output, precision )
