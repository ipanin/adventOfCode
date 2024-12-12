from functools import cache
res = 0
div= [ 1,  1,  1, 26,  1, 26, 26,  1,  1,  1, 26, 26, 26, 26]
a =  [13, 11, 15, -6, 15, -8, -4, 15, 10, 11,-11,  0, -8, -7]
b =  [ 3, 12,  9, 12,  2,  1,  1, 13,  1,  6,  2, 11, 10,  3]
N=14

def check_digit(digit, res, i):
    x = res % 26 + a[i]
    res //= div[i] # / div = 1 | 26
    
    if digit != x:
        res = res * 26 + digit + b[i]
    
    return res
    #mod = res / div[i] # / div = 1 | 26
    #rem = res % 26 
    #if digit != rem + a[i]:
    #    return mod * 26 + digit + b[i]
    #return mod

#def reverse(i, res):
#    for dig in range(9, 0, -1):
#        mod = res # digit == rem + a[i] 
#        rem =  dig - a[i] 
#        if 0 <= rem < 26:
#            res_prev = mod * div[i] + rem
            #if i == 13 && res_prev != 0
            #    mod = 0
            #    rem = 0 
@cache
def check_recurse(rank: int, res: int) -> str:
    i = N-1 - rank
#    if i == -1:
#        if res == 0:
#            return [0]
#        return []

    mod = res // div[i] # / div = 1 | 26
    rem = res % 26
    #for digit in range(9, 0, -1):
    for digit in range(1,10):
        if digit != rem + a[i]:
            res1 = mod * 26 + digit + b[i]
        else:
            res1 = mod

        if rank == 0:
            if res1 == 0: return str(digit)
            else: continue

        digits1 = check_recurse(rank-1, res1)
        if len(digits1):
            return str(digit) + digits1

    return ""

       
def solve1():
    for n in range(10**14-1, 10**13, -1):
        #if n % (10**13) == 0: print('.')
        if check(n):
            return n




dig = check_recurse(N-1, 0)
print(dig)