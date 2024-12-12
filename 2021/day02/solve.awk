#! /usr/bin/awk -f

/do/ { y += $2; }
/up/ { y -= $2; }
/fo/ { x += $2; y2 += y * $2 }
END { print "Part1:", x * y, "Part2:", x * y2 }