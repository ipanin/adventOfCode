import util


def solve1(rules, pages_arrays) -> int:
    result = 0
    for pages in pages_arrays:
        if is_order_correct(rules, pages):
            result += int(pages[len(pages)//2])
    return result


def is_order_correct(rules: list[tuple[str, str]], pages: list[str]) -> bool:
    for i in range(1, len(pages)):
        curr = pages[i]
        prev_items = pages[:i]
        for rule in rules:
            if rule[0] == curr and rule[1] in prev_items:
                return False
    return True


def solve2(rules, pages_arrays) -> int:
    result = 0
    for pages in pages_arrays:
        if not is_order_correct(rules, pages):
            pages = correct_order(rules, pages)
            result += int(pages[len(pages)//2])
    return result


def correct_order(rules: list[tuple[str, str]], pages: list[str]) -> list[str]:
    for i in range(1, len(pages)):
        curr = pages[i]
        prev_items = pages[:i]
        for left, right in rules:
            if left == curr and right in prev_items:
                ri = prev_items.index(right)
                pages[i] = right
                pages[ri] = curr
                return correct_order(rules, pages)
    return pages


rules_block, pages_block = util.load_str_blocks('input.txt')
rules = [line.split('|') for line in rules_block]
pages = [line.split(',') for line in pages_block]

util.assert_equal(solve1(rules, pages), 5268, "Part1")
util.assert_equal(solve2(rules, pages), 5799, "Part2")
