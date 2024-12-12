# only part 1
import util

def test(data, expected1, expected2):
    result = solve1(data)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve2(data)
    print("Part 2.", result)
    util.assert_equal(result, expected2)

def move(p, die):
    p += die % 10
    if p > 10: 
        p = p - 10
    die += 1
    if die > 100: die = 1
    return p, die

def solve1(data):
    '''
    a game board with a circular track containing ten spaces marked 1 through 10 
    Each player's starting pos == puzzle input.
    On each player's turn, the player rolls the die three times and adds up the results.
    Then, the player moves their pawn. Increase their score by the value of pos stopped on.
    Player wins if his score >= 1000.
    Deterministic dice: 100-sided die. This die always rolls 1 first, then 2, then 3, and so on up to 100, 
    after which it starts over at 1 again.
    '''
    p1, p2 = data
    die = 1
    score1 = score2 = 0
    nroll = 0
    while True:
        p1, die = move(p1, die)
        p1, die = move(p1, die)
        p1, die = move(p1, die)
        nroll += 3
        score1 += p1
        #print(f"Player 1 dice={dice}, pos={p1}, score={score1}")
        if score1 >= 1000:
            return score2*nroll
        p2, die = move(p2, die)
        p2, die = move(p2, die)
        p2, die = move(p2, die)
        nroll += 3
        score2 += p2
        #print(f"Player 2 dice={dice}, pos={p2}, score={score2}")
        if score2 >= 1000:
            return score1*nroll

def solve2(data):
    win_score = 21
    pass


test([4,8], 739785, 444356092776315)
test([3,7], 1006866, 0)