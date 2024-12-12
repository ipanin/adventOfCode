import util

def solve1(data) -> int:
    disk = inflate(data)
    compact(disk)
    return checksum(disk)

def inflate(data):
    disk = []
    is_file = True
    file_id = 0
    for d in data:
        if is_file:
            for _ in range(d):
                disk.append(file_id)
            is_file = False
            file_id += 1
        else:
            for _ in range(d):
                disk.append(None)
            is_file = True
    return disk

def compact(disk):
    i = 0
    while i<len(disk)-1:
        if disk[i] is not None:
            i+=1
            continue

        dj = disk.pop(-1)
        while dj is None:
            dj = disk.pop(-1)

        disk[i] = dj
        i+=1

# multiplying each position with the number it contains
def checksum(disk):
    return sum(i*d for i,d in enumerate(disk) if d is not None)


data = util.load_digit_list('input_sample.txt')
util.assert_equal(solve1(data), 1928, "Part1 sample")

data = util.load_digit_list('input.txt')
util.assert_equal(solve1(data), 6307275788409, "Part1")
