#!/usr/bin/awk -f
# хакерское решение с reddit

$3 { # cd commands
    n -= (-1~$3 ? !++S[n] - b[d--] : b[++d]=n)
}

{ n += $1 }

END {
    for(; d; n+=b[d--])
        S[n]++;
    for(; ++p2<n-4e7 || !S[p2]; )
        p2 > 1e5 || p1 += p2 * S[p2];
    print p1"\n"p2
}
