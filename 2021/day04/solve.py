# Day 4: Giant squid bingo
# Найти первую и последнюю выигравшую карточку лото.
# Решение за 1 проход с помощью генератора
import util

def test(fname, expected1, expected2):
    line, *blocks = util.load_str_blocks(fname)
    draw_numbers = [int(item) for item in line[0].split(',')]
    cards = [[[int(n) for n in row.split()] for row in block] for block in blocks]
    print("Loaded", fname)

    first, *_, last = win_scores(draw_numbers, cards)
    print("Part 1.", first)
    util.assert_equal(first, expected1)

    print("Part 2.", last)
    util.assert_equal(last, expected2)

# Generator
def win_scores(numbers,cards):
    won_card_numbers = set()
    for n in numbers:
        for i, card in enumerate(cards):
            if i not in won_card_numbers and mark(card, n):
                won_card_numbers.add(i)
                yield score(card, n)

def mark(card, n: int):
    for r, row in enumerate(card):
        for c, v in enumerate(row):
            if v == n:
                card[r][c] = None
                if all(x is None for x in row) or all(card[i][c] is None for i in range(len(card))):
                    return True
    return False

def score(card, n: int):
    res = 0
    for row in card:
        res += sum(c for c in row if c is not None)
    return res * n 

test("input_sample.txt", 4512, 1924)
test("input.txt", 11774, 4495)