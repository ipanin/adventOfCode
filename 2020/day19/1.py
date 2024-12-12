# AoC 2020. Day 19
import util

rules_sample_data = [
    '0: 4 1 5',
    '1: 2 3 | 3 2',
    '2: 4 4 | 5 5',
    '3: 4 5 | 5 4',
    '4: "a"',
    '5: "b"']

def match_pattern(msg, pattern, rules):
    if pattern.isalpha():
        return msg.startswith(pattern), len(pattern) # True, 1

    pattern_len = 0
    result = True
    for token in pattern.split(' '):
        num = int(token)
        res, L = match(msg[pattern_len:], rules[num], rules)
        pattern_len += L
        if not res:
            result = False

    return result, pattern_len

def match(msg, rule, rules):
    for pattern in rule:
        res, L = match_pattern(msg, pattern, rules)
        if res:
            return True, L
    return False, L

def simplify(rule: str, rules: dict) -> str:
    if rule.isalpha():
        return rule

    result = ""
    for r in rule.split(' '):
        if r == '|':
            result += r
        elif r.isalpha():
            result += r
        elif r.isnumeric():
            num = int(r)
            r1 = simplify(rules[num], rules)
            rules[num] = r1
            result += r1
    return result

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

rules_sample = parse(rules_sample_data)
#print(rules_sample)

util.assert_equal(match('ababbb',rules_sample[0], rules_sample), (True, 6))
util.assert_equal(match('abbbab',rules_sample[0], rules_sample), (True, 6))
util.assert_equal(match('bababa',rules_sample[0], rules_sample), (False, 6))
util.assert_equal(match('aaabbb',rules_sample[0], rules_sample), (False, 6))
util.assert_equal(match('aaaabbb',rules_sample[0], rules_sample), (True, 6))

rules_data = util.load_str_lines_list('input_rules.txt')
messages = util.load_str_lines_list('input_messages.txt')
result = solve1(messages, rules_data)
print("Part 1.", result)
util.assert_equal(result, 299)


