# AoC 2020. Day 16: Ticket Translation
import util


def get_valid_tickets(data, rules):
    result = []
    for line in data:
        validTicket = True
        ticket = [int(f) for f in line.split(',')]
        for f in ticket:
            validField = False
            for r1, r2, r3, r4 in rules:
                if (r1 <= f <= r2) or (r3 <= f <= r4):
                    validField = True
                    break
            if not validField:
                validTicket = False
                break
        if validTicket:
            result.append(ticket)
    return result


def solve2(data, rules, my):
    tickets = get_valid_tickets(data, rules)
    tickets.append(my) # if it helps
    H = len(tickets)
    W = len(tickets[0])
    colsByRule = {}
    for i, rule in enumerate(rules):
        r1, r2, r3, r4 = rule
        for rule in range(W):
            colMatch = True
            for row in range(H):
                field = tickets[row][rule]
                if not ((r1 <= field <= r2) or (r3 <= field <= r4)):
                    colMatch = False
                    break
            if colMatch:
                a = colsByRule.get(i, [])
                a.append(rule)
                colsByRule[i] = a
    #print(rulesByCol)
    colByRule = {}
    while len(colsByRule) > 0:
        for rule, colNums in colsByRule.items():
            if len(colNums) == 1:
                foundCol = colNums[0]
                colByRule[rule] = foundCol
                colsByRule.pop(rule)
                break
        for rule, colNums in colsByRule.items():
            if foundCol in colNums:
                colNums.remove(foundCol)
                colsByRule[rule] = colNums
    #print(colByRule)
    result = 1
    for i in range(6):
        col = colByRule[i]
        result *=  my[col]
    return result
            
        

rules_data = util.load_str_lines_list('input_rules.txt')
rules = []
for line in rules_data:
    r1, r2, r3, r4 = util.findall_ints(line)
    rules.append((r1,r2, r3, r4))

my = [73,53,173,107,113,89,59,167,137,139,71,179,131,181,67,83,109,127,61,79]
data = util.load_str_lines_list('input_tickets.txt')

result = solve2(data, rules, my)
print("Part 2.", result)
util.assert_equal(result, 910339449193)


