#!/usr/bin/awk -f

BEGIN { FS="," }

{
    for (i=1; i<=NF; i++)
        fish[$i]++ 
}

END {
    for (d=0; d<256; d++)
        fish[(d+7) % 9] += fish[d % 9]

    for (n in fish)
        sum += fish[n]

    print "Part2:", sum
}