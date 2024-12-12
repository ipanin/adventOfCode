# Day 2: Rock Paper Scissors
import util

score = { 'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3 }
rules = { (2,1):0, (3,2):0, (1,3):0, (1,1):3, (2,2):3, (3,3):3, (1,2):6, (2,3):6, (3,1):6 }

lines = util.load_str_lines("input.txt")
result = 0
for line in lines:
    x, y = line.split()
    score1 = score[x]
    score2 = score[y]
    round = score2 + rules[(score1,score2)]
    result += round
print('Part 1.', result)
util.assert_equal(result, 13009)