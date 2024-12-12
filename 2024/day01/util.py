import os
import re

NEAR4 = [-1, 1, -1j, 1j]
NEAR8 = [-1, 1, -1j, 1j, -1-1j, -1+1j, 1+1j, 1-1j]

def assert_equal(actual, expected):
    if actual != expected:
        print(f"Error, expected = {expected}, actual = {actual}")
    else:
        print("OK")

def assert_equal(actual, expected, name):
    if actual != expected:
        print(f"{name}. Error, expected = {expected}, actual = {actual}")
    else:
        print(f"{name}. {actual} - OK")

def full_name(fname: str) -> str:
    folder = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(folder, fname)

# 100
# 200
def load_int_lines(fname: str) -> list[int]:
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
def load_str_lines(fname: str) -> list[str]:
    data = []
    with open(full_name(fname), 'rt') as f:
        # return [line.rstrip() for line in f.readlines() if len(line.rstrip())]
        for line in f.readlines():
            x = line.rstrip()
            if len(x):
                data.append(x)

    return data

# 1,2,3
def load_int_list(fname: str) -> list[int]:
    with open(full_name(fname), 'rt') as f:
        line = f.readline().rstrip()
        return [int(item) for item in line.split(',')]

# 123
# loaded as [1, 2, 3]
def load_number_string_list(fname: str) -> list[int]:
    with open(full_name(fname), 'rt') as f:
        line = f.readline().rstrip()
        return [int(item) for item in line]

# aaa
# bbb
#
# ccc
# ddd
def load_str_blocks(fname: str) -> list[list[str]]:
    with open(full_name(fname), 'rt') as f:
        blocks = f.read().rstrip().split('\n\n')
        return [b.split('\n') for b in blocks]

regex = re.compile(r"\D*(\d+)\D*")

def findall_ints(s: str) -> list[int]:
    return [int(x) for x in regex.findall(s)]

def find_int(s: str) -> int:
    return int(regex.findall(s)[0])

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


def load_grid(fname: str) -> dict[complex, int]:
    # return {x+y*1j: int(c) for x,line in enumerate(open(fname)) for y,c in enumerate(line.strip())}
    grid = {}
    with open(full_name(fname), 'rt') as f:
        for y,line in enumerate(f):
            for x,c in enumerate(line.rstrip()):
                grid[x + y*1j] = int(c)
    return grid

def chunks(lst: list, chunk_size: int) -> list[list]:
    for pos in range(0, len(lst), chunk_size):
        yield lst[pos : pos+chunk_size]


class GrowingList(list):
    def __setitem__(self, index: int, value):
        if index >= len(self):
            self.extend([0]*(index + 1 - len(self)))
        list.__setitem__(self, index, value)
    
    def __getitem__(self, index: int):
        if index < len(self):
            return list.__getitem__(self, index)
        else:
            return 0


def rindex(alist, value):
    return len(alist) - alist[-1::-1].index(value) - 1

# range in positive or negative direction
def my_range(start: int, end: int):
    step = 1
    if start > end: 
        step = -1
    return range(start, end+step, step)

