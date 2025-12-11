a = b = i = 0

for l in open('input.txt'):
    for _ in range(int(l[1:])):
        i += {'L':-1, 'R':+1}[l[0]]
        if i % 100 == 50: b += 1
    if i % 100 == 50: a += 1

print(a, b)