import os
import re


def assert_equal(actual, expected):
    if actual != expected:
        print(f"Error, expected = {expected}, actual = {actual}")
    else:
        print("OK")


def full_name(fname):
    folder = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(folder, fname)

def load_int_lines_list(fname):
    data = []
    with open(full_name(fname), 'rt') as f:
        # return [int(line.rstrip('\n')) for line in f.readlines()]
        for line in f.readlines():
            x = line.rstrip('\n')
            if len(x):
                data.append(int(x))

    return data

def load_str_lines_list(fname):
    data = []
    with open(full_name(fname), 'rt') as f:
        # return [int(line.rstrip('\n')) for line in f.readlines()]
        for line in f.readlines():
            x = line.rstrip('\n')
            if len(x):
                data.append(x)

    return data

def load_int_list(fname):
    with open(full_name(fname), 'rt') as f:
        line = f.readline().rstrip('\n')
        return [int(item) for item in line.split(',')]

def load_number_string_list(fname):
    with open(full_name(fname), 'rt') as f:
        line = f.readline().rstrip('\n')
        return [int(item) for item in line]


def load_str_blocks(fname):
    with open(full_name(fname), 'rt') as f:
        blocks = f.read().rstrip().split('\n\n')
        return [b.split('\n') for b in blocks]

def chunks(lst, n):
    for pos in range(0, len(lst), n):
        yield lst[pos : pos+n]

class GrowingList(list):
    def __setitem__(self, index, value):
        if index >= len(self):
            self.extend([0]*(index + 1 - len(self)))
        list.__setitem__(self, index, value)
    
    def __getitem__(self, index):
        if index < len(self):
            return list.__getitem__(self, index)
        else:
            return 0


def findall_ints(s: str):
    return [int(x) for x in re.findall("\D*(\d+)\D*", s)]


def rindex(alist, value):
    return len(alist) - alist[-1::-1].index(value) - 1

