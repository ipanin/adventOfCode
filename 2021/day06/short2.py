with open('input.txt') as f:
    data = [int(x) for x in f.readline().split(',')]

# agegroup = [data.count(i) for i in range(9)]
# Longer, but requires only 1 iteration:
agegroup = [0] * 9 ## 0-8 days
for f in data: 
    agegroup[f] += 1

for d in range(256):
    agegroup[(d+7) % 9] += agegroup[d % 9]

print(sum(agegroup))
