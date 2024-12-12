# AoC 2020. Day 22
# Card game
from collections import deque
import util

def play(player1, player2):
    while len(player1) and len(player2):
        card1 = player1.popleft()
        card2 = player2.popleft()
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        elif card1 < card2:
            player2.append(card2)
            player2.append(card1)
        else:
            print("Same cards", card1)

def play_game(cards1, cards2, level):
#    if level == 0:
#        print("Game", cards1, cards2)
#    else:
#        print("Level", level)

    player1 = deque(cards1)
    player2 = deque(cards2)

    rounds1 = set(str(player1))
    rounds2 = set(str(player2))

    while len(player1) and len(player2):
        card1 = player1.popleft()
        card2 = player2.popleft()
        if card1 <= len(player1) and card2 <= len(player2):
            c1 = list(player1)[:card1]
            c2 = list(player2)[:card2]
            winner, _ = play_game(c1, c2, level+1)
            if winner == 1:
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)
        elif card1 > card2:
            player1.append(card1)
            player1.append(card2)
        elif card1 < card2:
            player2.append(card2)
            player2.append(card1)
        else:
            print("Same cards", card1)
        
        # infinite game prevention
        if str(player1) in rounds1 and str(player2) in rounds2:
            return 1, player1
    
        rounds1.add(str(player1))
        rounds2.add(str(player2))
    
    if len(player1):
        return 1, player1
    else:
        return 2, player2

def score(player):
    res = 0
    i = 1
    while len(player):
        res += player.pop() * i
        i +=1

    return res

def solve1(cards1: list, cards2: list) -> int:
    player1 = deque(cards1)
    player2 = deque(cards2)

    play(player1, player2)
    
    return score(player1) + score(player2)

def solve2(cards1: list, cards2: list) -> int:
    winner, player = play_game(cards1, cards2, 0)
   
    return score(player)

def load_cards(fname):
    data = util.load_str_blocks(fname)
    return [int(line) for line in data[0][1:]], [int(line) for line in data[1][1:]]

cards1, cards2 = load_cards('input.txt')
result = solve1(cards1, cards2)
print("Part 1.", result)
util.assert_equal(result, 30197)

winner, cards = play_game([43,19], [2,29,14], 0)
util.assert_equal(winner, 1)

util.assert_equal(solve2([9, 2, 6, 3, 1], [5, 8, 4, 7, 10]), 291)

result = solve2(cards1, cards2)
print("Part 2.", result)
util.assert_equal(result, 34031)


