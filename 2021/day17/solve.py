import util

'''
Part1; ymin*(ymin+1)/2 not always work
target area: x=352..377, y=-49..-30
The solution: 66, and not 1176 = 49*48/2
'''

def test(title, data, expected1, expected2):
    part1, part2 = solve(data)
    print(title, "part 1.", part1)
    util.assert_equal(part1, expected1)

    print(title, "part 2.", part2)
    util.assert_equal(part2, expected2)

def solve(data):
    xmin, xmax, ymin, ymax = data
    vxmin = 1
    vxmax = xmax
    vymin = ymin
    vymax = 1000
    
    yy = [shoot(vx, vy, xmin, xmax, ymin, ymax) for vx in range(vxmin, vxmax+1) for vy in range(vymin, vymax+1)]
    return max(yy), sum(1 for y in yy if y != -1000)

def shoot(vx0, vy0, xmin, xmax, ymin, ymax):
    vx = vx0; vy = vy0
    x = y = maxy = 0
    while(True):
        x += vx
        y += vy
        if y > maxy: maxy = y

        if vx > 0: vx -= 1
        vy -= 1

        if x > xmax: break
        if y < ymin: break
        if vx == 0 and (x < xmin or x > xmax): break
        
        target = x in range(xmin, xmax+1) and y in range(ymin, ymax+1)
        if target: 
            #print(vx0, vy0, maxy)
            return maxy 
    return -1000

test("Sample", [20, 30, -10,-5], 45, 112)
test("Task", [150,193, -136,-86], 9180, 3767)