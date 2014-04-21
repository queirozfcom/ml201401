import helpers.types as types

# TODO unit test this

# just apply the returned normalizer for each element. Simple, uh?
def normalize(l):
    return map(get_normalizer_for(l),l)


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

# unless all attributes are of a single type (e.g. number), type is string.
# should we define a threshold to account for bad data? (e.g. a list where 
#    every element is a number except for something like "324W" - this is 
#    probably noise, I shouldn't consider everything to be strings just bec
#    ause of this.)
def _get_type(l):
    if all(is_number(el) for el in l):
        return 'number'
    elif all(is_date(el) for el in l):
        return 'date'
    else:
        return 'string'

#convert everything to lower case or upper case
#remove special characters?
#disregard whitespace/newline?
#remove quotes, inverted commas around text
def _string_normalizer(l):
    return lambda element: return element

#normalize to (MAX_VALUE - MIN_VALUE)
def _number_normalizer(line):
    return lambda element: return element

#convert everything to a single date Format
def _date_normalizer(line):
    return lambda element: return element