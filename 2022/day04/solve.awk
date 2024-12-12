#! /usr/bin/awk -f

BEGIN { FS=",|-" }

$3 <= $1 && $2 <= $4 || $1 <= $3 && $4 <= $2 { part1++ }
$1 <= $4 && $3 <= $2 { part2++ }

END { print(part1, part2) }

# one-liner for part2:
# awk -F",|-" '$1<=$4&&$3<=$2{a++}END{print a}' input.txt

# one-liner for part 1 & 2:
# awk -F",|-" '$3<=$1&&$2<=$4||$1<=$3&&$4<=$2{p1++}$1<=$4&&$3<=$2{p2++}END{print p1,p2}' input.txt