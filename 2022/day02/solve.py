# Day 2: Rock Paper Scissors
# подсчет результатов игры по списку ходов
# В части 2 свой ход надо определить по итогу раунда
import util


def test(filename, expected1, expected2):
    data = util.load_str_lines(filename)
    print(filename, "loaded")

    result = solve1(data)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve2(data)
    print("Part 2.", result)
    util.assert_equal(result, expected2)


def solve1(data):
    score = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    rules = {(2, 1): 0, (3, 2): 0, (1, 3): 0, (1, 1): 3, (2, 2): 3, (3, 3): 3, (1, 2): 6, (2, 3): 6, (3, 1): 6}

    total = 0
    for line in data:
        shape1, shape2 = line.split()
        shape_score1 = score[shape1]
        shape_score2 = score[shape2]
        round = shape_score2 + rules[(shape_score1, shape_score2)]
        total += round
    return total


def solve2(data):
    score = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}
    rules = {(2, 0): 1, (3, 0): 2, (1, 0): 3, (1, 3): 1, (2, 3): 2, (3, 3): 3, (1, 6): 2, (2, 6): 3, (3, 6): 1}

    total = 0
    for line in data:
        shape1, shape2 = line.split()
        shape_score1 = score[shape1]
        my_round_score = score[shape2]
        shape_score2 = rules[(shape_score1, my_round_score)]
        total += shape_score2 + my_round_score
    return total


test("input.txt", 13009, 10398)