from parse import *

rules = { 
    search('{} bag', x)[0]: [*findall('{:d} {} bag', x)]
    for x in open('day07/input.txt') 
}

t = 'shiny gold'
def f(c): return any(d==t or f(d) for _,d in rules[c])
def g(c): return sum(n + n * g(d) for n,d in rules[c])
print(sum(map(f, rules)), g(t))

###

import re

rules = { 
    re.findall('(.+?) bag', x)[0]: [*re.findall(r'(\d+) (.+?) bag', x)] 
    for x in open('day07/input.txt') 
}

t = 'shiny gold'
def f2(c): return any(d==t or f2(d) for _,d in rules[c])
def g2(c): return sum(int(n) * (1 + g2(d)) for n,d in rules[c])
print(sum(map(f2, rules)), g2(t))