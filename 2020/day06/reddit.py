with open('day06/input.txt') as f:
    groups = f.read().strip().split('\n\n')

print(sum(len(set.union(*map(set, g.split('\n')))) for g in groups))
print(sum(len(set.intersection(*map(set, g.split('\n')))) for g in groups))

# ruby
# p read.split("\n\n").map{|x|x.split.join.chars.uniq.size}.sum
# p read.split("\n\n").map{|x|x.lines.map{|x|x.chomp.chars}.reduce(:&).size}.sum

# Haskell
# sum $ map(length . foldr1 union) input
# sum $ map(length . foldr1 intersect) input
