import os
import re

NEAR4 = [-1, 1, -1j, 1j]
NEAR8 = [-1, 1, -1j, 1j, -1-1j, -1+1j, 1+1j, 1-1j]

def assert_equal(actual, expected):
    if actual != expected:
        print(f"Error, expected = {expected}, actual = {actual}")
    else:
        print("OK")

def full_name(fname):
    folder = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(folder, fname)

# 100
# 200
def load_int_lines(fname):
    data = []
    with open(full_name(fname), 'rt') as f:
        # return [int(line.rstrip('\n')) for line in f.readlines()]
        for line in f.readlines():
            x = line.rstrip('\n')
            if len(x):
                data.append(int(x))

    return data

# aaa
# bbb
def load_str_lines(fname):
    data = []
    with open(full_name(fname), 'rt') as f:
        # return [line.rstrip() for line in f.readlines() if len(line.rstrip())]
        for line in f.readlines():
            x = line.rstrip()
            if len(x):
                data.append(x)

    return data

# 1,2,3
def load_int_list(fname):
    with open(full_name(fname), 'rt') as f:
        line = f.readline().rstrip()
        return [int(item) for item in line.split(',')]

# 123
# loaded as [1, 2, 3]
def load_number_string_list(fname):
    with open(full_name(fname), 'rt') as f:
        line = f.readline().rstrip()
        return [int(item) for item in line]

# aaa
# bbb
#
# ccc
# ddd
def load_str_blocks(fname):
    with open(full_name(fname), 'rt') as f:
        blocks = f.read().rstrip().split('\n\n')
        return [b.split('\n') for b in blocks]


def findall_ints(s: str):
    return [int(x) for x in re.findall(r"\D*(\d+)\D*", s)]


# 1,2->3,4
# 4,5->6,7
def load_int_lists(fname):
    data = []
    with open(full_name(fname), 'rt') as f:
        for line in f.readlines():
            nums = findall_ints(line)
            if len(nums):
                data.append(nums)

    return data


def load_grid(fname):
    # return {x+y*1j: int(c) for x,line in enumerate(open(fname)) for y,c in enumerate(line.strip())}
    grid = {}
    with open(full_name(fname), 'rt') as f:
        for y,line in enumerate(f):
            for x,c in enumerate(line.rstrip()):
                grid[x + y*1j] = int(c)
    return grid

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


def rindex(alist, value):
    return len(alist) - alist[-1::-1].index(value) - 1

# range in positive or negative direction
def my_range(start, end):
    step = 1
    if start > end: 
        step = -1
    return range(start, end+step, step)