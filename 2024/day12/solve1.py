import util

def solve1(matrix) -> int:
    types: dict[str, list[complex]] = {}
    for coord, plant in matrix.items():
        if plant in types:
            types[plant].append(coord)
        else:
            types[plant] = [coord]

    res = 0
    for _, coords in types.items():
        res += sum(price(region) for region in get_regions(coords))
    return res

def get_regions(coords):
    result = []
    while len(coords)>0:
        coord = coords.pop()
        region = []
        edge = [coord]
        while len(edge) > 0:
            edge_next = []
            for e in edge:
                for n in util.NEAR4:
                    ncoord = e + n
                    if ncoord in coords:
                        coords.remove(ncoord)
                        edge_next.append(ncoord)

            region += edge
            edge = edge_next
        result.append(region)
    return result

def price(coords):
    fence = 0
    for coord in coords:
        for n in util.NEAR4:
            if coord + n not in coords:
                fence += 1
    return len(coords) * fence


matrix = util.load_char_matrix('sample3.txt')
util.assert_equal(solve1(matrix), 1930, "Part 1, sample 3")


matrix = util.load_char_matrix('input.txt')
util.assert_equal(solve1(matrix), 1381056, "Part 1")
