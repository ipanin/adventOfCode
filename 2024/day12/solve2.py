import util

def solve2(matrix) -> int:
    types: dict[str, list[complex]] = {}
    for coord, plant in matrix.items():
        if plant in types:
            types[plant].append(coord)
        else:
            types[plant] = [coord]

    res = 0
    for _, coords in types.items():
        res += sum(price2(region) for region in get_regions(coords))
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

def price2(coords):
    angles = 0
    for coord in coords:
        for n in util.NEAR4:
            neib = [coord + n, coord + n + n*1j, coord + n*1j]
            fig = [neib[0] in coords, neib[1] in coords, neib[2] in coords]
            if fig in [[True, False, True], [False, False, False], [False, True, False]]:
                angles += 1

    return len(coords) * angles

matrix = util.load_char_matrix('sample1.txt')
util.assert_equal(solve2(matrix), 236, "Part 2, sample 1")

matrix = util.load_char_matrix('sample2.txt')
util.assert_equal(solve2(matrix), 368, "Part 2, sample 2")

matrix = util.load_char_matrix('sample3.txt')
util.assert_equal(solve2(matrix), 1206, "Part 2, sample 3")

matrix = util.load_char_matrix('input.txt')
util.assert_equal(solve2(matrix), 834828, "Part 2")
