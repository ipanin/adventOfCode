# AoC 2020. Day 16: Ticket Translation
# Определить, где какие поля в билетах на основании допустимых диапазонов.
# AoC 2020. Day 16: Ticket Translation
import util

def field_valid(field: int, rules: list) -> bool:
    for r1, r2, r3, r4 in rules:
        if (r1 <= field <= r2) or (r3 <= field <= r4):
            return True
    return False

def solve1(tickets, rules):
    result = 0
    for ticket in tickets:
        #result += sum(filter(lambda f:not field_valid(f,rules), [int(field) for field in ticket.split(',')]))
        for field in ticket.split(','):
            f = int(field)
            if not field_valid(f, rules):
                result += f
    return result

###

def ticket_valid(ticket: list, rules: list) -> bool:
    for field in ticket:
        if not field_valid(field, rules):
            return False
    return True

def get_valid_tickets(data, rules):
    valid_tickets = []
    for line in data:
        ticket = [int(field) for field in line.split(',')]
        if ticket_valid(ticket, rules):
            valid_tickets.append(ticket)
    return valid_tickets

def findAllCols(tickets, rules):
    H, W = len(tickets), len(tickets[0])
    colsByRule = {}
    for i, item in enumerate(rules):
        r1, r2, r3, r4 = item
        for ruleN in range(W):
            colMatch = True
            for row in range(H):
                field = tickets[row][ruleN]
                if not ((r1 <= field <= r2) or (r3 <= field <= r4)):
                    colMatch = False
                    break
            if colMatch:
                a = colsByRule.get(i, [])
                a.append(ruleN)
                colsByRule[i] = a
    return colsByRule

def findOneCol(colsByRule):
    colByRule = {}
    while len(colsByRule) > 0:
        for ruleN, colNums in colsByRule.items():
            if len(colNums) == 1:
                foundCol = colNums[0]
                colByRule[ruleN] = foundCol
                colsByRule.pop(ruleN)
                break
        for ruleN, colNums in colsByRule.items():
            if foundCol in colNums:
                colNums.remove(foundCol)
                colsByRule[ruleN] = colNums
    return colByRule

def solve2(data, rules, my):
    tickets = get_valid_tickets(data, rules)
    tickets.append(my) # if it helps
    
    colsByRule = findAllCols(tickets, rules)
    colByRule = findOneCol(colsByRule)

    result = 1
    for i in range(6):
        col = colByRule[i]
        result *=  my[col]
    return result
        

tickets = util.load_str_lines_list('input_tickets.txt')
my_ticket = [73,53,173,107,113,89,59,167,137,139,71,179,131,181,67,83,109,127,61,79]
rules_data = util.load_str_lines_list('input_rules.txt')
rules = []
for line in rules_data:
    limits = util.findall_ints(line)
    rules.append(limits)

result = solve1(tickets, rules)
print("Part 1.", result)
util.assert_equal(result, 20975)

result = solve2(tickets, rules, my_ticket)
print("Part 2.", result)
util.assert_equal(result, 910339449193)


