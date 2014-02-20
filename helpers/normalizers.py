
#return a function that should be applied to each attribute in order to "normalize" it
def get_normalizer_for(l):

	type=get_type(l)

	if type == 'string':
		return _string_normalizer(l)
	elif type == 'number':
		return _number_normalizer(l)
	elif type == 'date':
		return _date_normalizer(l)
	else:
		raise Exception('Unknown type for attribute list given')

#TODO unit test this

#unless all attributes are of a single type (e.g. number), type is string
#should we define a threshold to account for bad data (e.g. a list where every element is a number except for something like "324W" - this is probably noise, I shouldn't consider everything to be strings just because of this.)
def _get_type(l):

	return 'string'

#convert everything to lower case or upper case
#remove special characters?
#disregard whitespace/newline?
#remove quotes, inverted commas around text
def _string_normalizer(line):
	return lambda line: return line

#normalize to (MAX_VALUE - MIN_VALUE)
def _number_normalizer(l):
	return lambda line: return line

#convert everything to a single Format
def _date_normalizer(l):
	return lambda line: return line