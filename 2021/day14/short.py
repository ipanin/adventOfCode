'''
tracking pair and character counts in two Counter dictionaries. For each replacement:
    decrease the count of the original pair,
    increase the count of the two replacement pairs,
    increase the count of new character.
This has two advantages: 1) we keep using the same dictionary throughout the steps, and 2) we don't have to compute the individual counts at the end.
from collections import Counter
'''
from collections import Counter

tpl, _, *rules = open(0).read().split('\n')
rules = dict(r.split(" -> ") for r in rules)
pairs = Counter(map(str.__add__, tpl, tpl[1:]))
chars = Counter(tpl)

for _ in range(40):
    for (a,b), c in pairs.copy().items():
        x = rules[a+b]
        pairs[a+b] -= c
        pairs[a+x] += c
        pairs[x+b] += c
        chars[x] += c

print(max(chars.values())-min(chars.values()))
