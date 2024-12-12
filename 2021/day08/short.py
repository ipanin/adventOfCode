# from https://www.reddit.com/r/adventofcode/comments/rbj87a/comment/hnoyy04/?utm_source=share&utm_medium=web2x&context=3 
import util
res = 0
for left, right in [line.split('|') for line in open(util.full_name('input.txt'))]:  # split signal and output
    l = {len(s): set(s) for s in left.split()}    # get number of segments

    n = ''
    for o in map(set, right.split()): # loop over output digits
        match len(o), len(o & l[4]), len(o & l[2]):  # mask with known digits (4seg=4, 2seg=1)
            case 2,_,_: n += '1'
            case 3,_,_: n += '7'
            case 4,_,_: n += '4'
            case 7,_,_: n += '8'
            
            case 5,2,_: n += '2'
            case 5,3,1: n += '5'
            case 5,3,2: n += '3'

            case 6,4,_: n += '9'
            case 6,3,1: n += '6'
            case 6,3,2: n += '0'
    
    res += int(n)

print(s)