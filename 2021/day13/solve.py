# Day 13: Transparent Origami
# Складываем поле пополам, в конце проявляется текст
import util
import gutil

def test(filename, expected1):
    grid, folds = load(filename)
    print(filename, "loaded")

    result = solve1(grid, folds)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    solve2(grid, folds)


def solve1(grid, folds):
    g1 = do_fold(grid, folds[0])
    return len(g1)


def solve2(grid, folds):
    for command in folds:
        grid = do_fold(grid, command)
        
    w = max(x for x,y in grid) + 1
    h = max(y for x,y in grid) + 1
    gutil.draw_image_bw(grid,w,h)


def do_fold(grid, command):
    cmd, pos = command.split('=')
    pos = int(pos)
    grid1 = set()
    for x,y in grid:
        if cmd == 'fold along x' and x > pos:
            x = 2*pos - x
        elif cmd == 'fold along y' and y > pos:
            y = 2*pos - y
    
        grid1.add((x,y))
    
    return grid1


def load(fname):
    with open(util.full_name(fname), 'rt') as f:
        coords, folds = f.read().rstrip().split('\n\n')

    points = []
    for line in coords.split('\n'):
        x,y = line.split(',')
        points.append((int(x), int(y)))
    
    return points, folds.split('\n')


test("input_sample.txt", 17)
test("input.txt", 704)