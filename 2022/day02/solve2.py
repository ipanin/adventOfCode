import util

score = { 'A':1, 'B':2, 'C':3, 'X':0, 'Y':3, 'Z':6 }
rules = { (2,0):1, (3,0):2, (1,0):3, (1,3):1, (2,3):2, (3,3):3, (1,6):2, (2,6):3, (3,6):1}

lines = util.load_str_lines("input.txt")
total = 0
for line in lines:
    shape1, shape2 = line.split()
    shape_score1 = score[shape1]
    my_round_score = score[shape2]
    shape_score2 = rules[(shape_score1, my_round_score)]
    total += shape_score2 + my_round_score

print('Part 2.', total)
util.assert_equal(total, 10398)