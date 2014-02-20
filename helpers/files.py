from helpers.types import is_number

def file_len(fname):
    num_headers = 0

    with open(fname) as f:
        for idx, line in enumerate(f):
            if is_header(line):
                num_headers += 1


    return idx + 1 - num_headers

def is_header(line):
    for el in line.split(','):
        if is_number(el):
            return False

    return True

