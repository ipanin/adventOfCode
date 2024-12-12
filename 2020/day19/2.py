# AoC 2020. Day 19: Monster messages
import util

def match_pattern(msg, pattern, rules):
    if pattern.isalpha():
        return msg.startswith(pattern), len(pattern) # True, 1

    pattern_len = 0
    result = True
    for token in pattern.split(' '):
        num = int(token)
        if pattern_len >= len(msg):
            return False, pattern_len

        res, L = match(msg[pattern_len:], rules[num], rules)
        pattern_len += L
        if not res:
            return False, pattern_len

    return result, pattern_len

def match(msg, rule, rules):
    for pattern in rule:
        res, L = match_pattern(msg, pattern, rules)
        if res:
            return True, L
    return False, L

def parse(rules_data):
    rules = {}
    for line in rules_data:
        num, rule = line.split(': ')
        if rule.startswith('"'):
            rule = rule[1]
        patterns = rule.split(' | ')
        rules[int(num)] = patterns
    
#    for k, v in rules.items():
#        rules[k] = simplify(v, rules)
    
    return rules

# How many messages completely match rule 0?
def solve1(messages, rules_data):
    rules = parse(rules_data)
    result = 0
    for msg in messages:
        res, L = match(msg, rules[0], rules)
        if res and L == len(msg):
            result += 1
    return result

def solve2(messages, rules_data):
    rules = parse(rules_data)
#    rules[8] = ["42 8", "42" ]
#    rules[11] = ["42 11 31", "42 31"]
    rules[0] = [
        "42 42 42 42 42 42 42 42 42 31", # max len = 80, len(rules[42]) == len(rules[42]) == 8
        "42 42 42 42 42 42 42 42 31 31",
        "42 42 42 42 42 42 42 31 31 31",
        "42 42 42 42 42 42 31 31 31 31",

        "42 42 42 42 42 42 42 42 31",
        "42 42 42 42 42 42 42 31 31",
        "42 42 42 42 42 42 31 31 31",
        "42 42 42 42 42 31 31 31 31",

        "42 42 42 42 42 42 42 31",
        "42 42 42 42 42 42 31 31",
        "42 42 42 42 42 31 31 31",

        "42 42 42 42 42 42 31",
        "42 42 42 42 42 31 31",
        "42 42 42 42 31 31 31",

        "42 42 42 42 42 31",
        "42 42 42 42 31 31",

        "42 42 42 42 31",
        "42 42 42 31 31",

        "42 42 42 31",
        "42 42 31", 
    ]

    result = 0
    for msg in messages:
        res, L = match(msg, rules[0], rules)
        if res and L == len(msg):
            result += 1
    return result

rules_sample_data = [
    '0: 4 1 5',
    '1: 2 3 | 3 2',
    '2: 4 4 | 5 5',
    '3: 4 5 | 5 4',
    '4: "a"',
    '5: "b"']

rules_sample = parse(rules_sample_data)
#print(rules_sample)

util.assert_equal(match('ababbb',rules_sample[0], rules_sample), (True, 6))
util.assert_equal(match('abbbab',rules_sample[0], rules_sample), (True, 6))
util.assert_equal(match('bababa',rules_sample[0], rules_sample), (False, 1))
util.assert_equal(match('aaabbb',rules_sample[0], rules_sample), (False, 2))
util.assert_equal(match('aaaabbb',rules_sample[0], rules_sample), (True, 6))

#rules_data = util.load_str_lines_list('input_rules_test2.txt')
#messages = util.load_str_lines_list('input_messages_test2.txt')
#util.assert_equal(solve1(messages, rules_data), 3)
#util.assert_equal(solve2(messages, rules_data), 12)


print("Part 1.")
rules_data = util.load_str_lines_list('input_rules.txt')
messages = util.load_str_lines_list('input_messages.txt')
util.assert_equal(solve1(messages, rules_data), 299)

print("Part 2.")
util.assert_equal(solve2(messages, rules_data), 414)


