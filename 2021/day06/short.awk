#!/usr/bin/awk -f

BEGIN { DAYS = 256; RS = "," }
      { a[$1]++ }
END   {
	for (i = 0; i < DAYS; i++)
		a[(i + 7) % 9] += a[i % 9]
	for (i in a)
		n += a[i]
	print n
}

# in one-liner form:
# awk 'BEGIN{RS=","}{a[$1]++}END{for(i=0;i<256;i++)a[(i+7)%9]+=a[i%9];for(i in a)n+=a[i];print n}' input.txt
