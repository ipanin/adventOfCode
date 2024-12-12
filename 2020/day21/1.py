# AoC 2020. Day 21: Allergen Assessment
import util

def parse(data):
    foods = []
    for line in data:
        ingrid_str, allerg_str = line.split(' (contains ')
        i = ingrid_str.split(' ')
        a = allerg_str[:-1].split(', ')
        foods.append((i, a))
    return foods

def detect_allerg(foods):
    all_allerg = set()
    for ingr, allerg in foods:
        all_allerg.update(set(allerg))
    
    res = dict()
    for a in all_allerg:
        susp_ingr = set()
        for ingr, allerg in foods:
            if a in allerg:
                if len(susp_ingr) == 0:
                    susp_ingr = set(ingr)
                else:
                    susp_ingr.intersection_update(set(ingr))
        res[a] = susp_ingr
    
    updated = True
    while updated:
        updated = False
        for a, i in res.items():
            if len(i) == 1:
                i1 = list(i)[0]
                for a2, i2 in res.items():
                    if a!=a2 and i1 in i2:
                        i2.remove(i1)
                        updated = True

    for a, i in res.items():
        res[a] = i.pop()

    return res

def solve1(foods):
    ingrByAllerg = detect_allerg(foods)
    all_allerg_ingr = set()
    for a, i in ingrByAllerg.items():
        all_allerg_ingr.add(i)
    
    res = 0
    for ingr, allerg in foods:
        for i in ingr:
            if i not in all_allerg_ingr:
                res += 1
    return res


def solve2(foods):
    ingrByAllerg = detect_allerg(foods)
    all_allerg_ingr = []
    
    for a in sorted(ingrByAllerg.keys()):
        all_allerg_ingr.append(ingrByAllerg[a])

    return ",".join(all_allerg_ingr)

data = util.load_str_lines('input.txt')
foods = parse(data)
result = solve1(foods)
print("Part 1.", result)
#util.assert_equal(result, 0)
result = solve2(foods)
print("Part 2.", result)
