import util

def solve2(data) -> int:
    disk, max_file_id = inflate2(data)
    compact2(disk, max_file_id)
    return checksum2(disk)

def inflate2(data):
    disk = []
    is_file = True
    file_id = 0
    for d in data:
        if is_file:
            disk.append((file_id, d))
            file_id += 1
        elif d>0:
            disk.append((None, d))
        is_file = not is_file
    return (disk, file_id-1)


def compact2(disk, max_file_id):
    file_id = max_file_id
    j = len(disk)-1
    while j>0:
        dj = disk[j]

        if dj[0] is None or dj[0] > file_id:
            j-=1
            continue

        # place dj to first free space
        i = 0
        while i<j:
            i+=1
            di = disk[i]
            if di[0] is None and di[1] >= dj[1]:
                if di[1] == dj[1]:
                    disk[i] = dj
                    disk[j] = (None, dj[1])
                else:
                    disk[i] = (None, di[1]-dj[1])
                    disk[j] = (None, dj[1])
                    disk.insert(i, dj)
                    j += 1

                break

        j-=1
        file_id -= 1

def checksum2(disk):
    result = 0
    pos = 0
    for d in disk:
        if d[0] is None:
            pos += d[1]
        else:
            for _ in range(d[1]):
                result += d[0]*pos
                pos += 1
    return result

data = util.load_digit_list('input_sample.txt')
util.assert_equal(solve2(data), 2858, "Part2 sample")

data = util.load_digit_list('input.txt')
util.assert_equal(solve2(data), 6327174563252, "Part2")
