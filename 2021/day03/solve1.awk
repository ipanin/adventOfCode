#! /usr/local/bin/gawk -f

BEGIN { FS="" }

{
	for (i=1; i<=NF; i++) {
		stat[i] += $i
	}
}

END {
	for (i=1; i<=NF; i++) {
		most = stat[i] > NR/2
		bit = lshift(1, NF-i)
		gamma += most * bit
		epsilon += !most * bit
	}
	
	print "Part1:", gamma*epsilon 
}