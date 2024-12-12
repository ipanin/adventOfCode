#! /usr/local/bin/gawk -f

# Сложновато получилось из-за того что разбор идет не построчно, а сразу по всем элементам.
BEGIN { FS="" }

{
    for (i=1; i<= NF; i++) {
        O2[NR][i] = CO2[NR][i] = $i
    }
}

function most_common(arr, n) {
    count = 0
    sum = 0
    for (i in arr) {
        count++
        if (arr[i][n] == 1) sum++
    }

    return sum >= count/2
}

function filter(arr, bit_n, target) {
    len = 0
    for (i in arr) {
        if (arr[i][bit_n] == target) {
            len++
        } else {
            delete arr[i]
        }
    }
    print bit_n, target, len
    return len
}

function bin2i(arr) {
    res = 0
    for (i in arr) {
        if (arr[i] == 1) {
            res += lshift(1, NF-i)
        }
    }
    return res
}

function applyCriteriaO2(arr) {
    bit_n = 1
    do {
        common = most_common(arr, bit_n)
        arr_len = filter(arr, bit_n, common)
        bit_n++
    } while (arr_len > 1)
    
    for (i in arr) {
        return bin2i(arr[i])
    }
}

function applyCriteriaCO2(arr) {
    bit_n = 1
    do {
        less_common = !most_common(arr, bit_n)
        arr_len = filter(arr, bit_n, less_common)
        bit_n++
    } while (arr_len > 1)
    
    for (i in arr) {
        return bin2i(arr[i])
    }
}

END {
    oxygen_rate = applyCriteriaO2(O2)
    diox_rate = applyCriteriaCO2(CO2)
    print "Part2:", oxygen_rate * diox_rate
}