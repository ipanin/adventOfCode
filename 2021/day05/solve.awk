#! /usr/bin/awk -f

BEGIN { FS = ",| -> " }

{
    x1 = $1; y1 = $2; x2 = $3; y2 = $4
    dx = x1 > x2 ? -1 : (x1 < x2)
    dy = y1 > y2 ? -1 : (y1 < y2)
    
    while (1) {
        part2[x1, y1]++
        if (dx == 0 || dy == 0) part1[x1, y1]++
        if (x1 == x2 && y1 == y2) break
        x1 += dx; y1 += dy
    }
}

END {
    for (i in part1) res1 += part1[i] > 1;
    print "Part1:", res1

    for (i in part2) res2 += part2[i] > 1;
    print "Part2:", res2
}