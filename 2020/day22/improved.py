# AoC 2020. Day 22
# Card game
import util

def play1(cards1, cards2):
    player1 = cards1.copy()
    player2 = cards2.copy()

    while player1 and player2:
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1 > card2:
            player1 += [card1, card2]
        elif card1 < card2:
            player2 += [card2, card1]
        else:
            print("Same cards", card1)
    
    if len(player1):
        return 1, player1
    else:
        return 2, player2

def play_game2(cards1, cards2):
    rounds = set()

    while cards1 and cards2:
        # infinite game prevention
        s = tuple(cards1), tuple(cards2) # str(cards1) + '|' + str(cards2)
        if s in rounds:
            return 1
        rounds.add(s)

        c1 = cards1.pop(0)
        c2 = cards2.pop(0)
        if c1 <= len(cards1) and c2 <= len(cards2):
            winner = play_game2(cards1[:c1], cards2[:c2])
        else:
            winner = 1 if c1 > c2 else 2

        if winner == 1:
            cards1 += [c1, c2]
        else:
            cards2 += [c2, c1]
    
    return 1 if cards1 else 2

def score(cards):
    return sum((i*card for i, card in enumerate(reversed(cards), 1)))

def solve1(cards1: list, cards2: list) -> int:
    winner, cards = play1(cards1, cards2)
    return score(cards)

def solve2(cards1: list, cards2: list) -> int:
    p1 = cards1.copy()
    p2 = cards2.copy()
    winner = play_game2(p1, p2)
    return score(p1) + score(p2)

def load_cards(fname):
    data = util.load_str_blocks(fname)
    return (
        [int(line) for line in data[0][1:]], 
        [int(line) for line in data[1][1:]]
    )

cards1, cards2 = load_cards('input.txt')

print("Part 1.")
util.assert_equal(solve1(cards1, cards2), 30197)

print("Part 2.")
util.assert_equal(play_game2([43,19], [2,29,14]), 1)

util.assert_equal(solve2([9, 2, 6, 3, 1], [5, 8, 4, 7, 10]), 291)
util.assert_equal(solve2(cards1, cards2), 34031)


