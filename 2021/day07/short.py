from numpy import median, mean, fromfile, floor, ceil

data = fromfile(open('input.txt'), int, sep=',')

#data.sort()
#target = data[len(data)//2] # median
target1 = int(median(data))
print("Part 1: ", sum(abs(data - target1)))

fuel = lambda d: d * (d+1) // 2
m = mean(data)
target1 = int(floor(m))
target2 = int(ceil(m))
res1 = sum(fuel(abs(data - target1)))
res2 = sum(fuel(abs(data - target2)))
print("Part 2: ", min(res1, res2))

#for target in range(min(data), max(data)+1):
#    res = min(res, sum(fuel(abs(x-target)) for x in data))