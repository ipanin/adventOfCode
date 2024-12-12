# AoC 2020. Day 16: Ticket Translation
import util


def solve(tickets, rules):
    result = 0
    for ticket in tickets:
        for field in ticket.split(','):
            f = int(field)
            valid = False
            for r1, r2 in rules:
                if r1 <= f <= r2:
                    valid = True
                    break
            if not valid:
                result += f
    return result


tickets = util.load_str_lines_list('input_tickets.txt')
rules_data = util.load_str_lines_list('input_rules.txt')
rules = []
for line in rules_data:
    r1, r2, r3, r4 = util.findall_ints(line)
    rules.append((r1,r2))
    rules.append((r3,r4))

result = solve(tickets, rules)
print("Part 1.", result)
util.assert_equal(result, 20975)


