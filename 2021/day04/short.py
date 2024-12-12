# From https://www.reddit.com/r/adventofcode/comments/r8i1lq/comment/hn982og/
'''
Using a 4-dimensional NumPy array to store marked numbers for all boards and all rounds. 
This way, we don't need any loops or comprehensions!
Here m is a 4-D matrix containing each board after drawing each number. 
It indicates whether a position on a board has been drawn in a round (or before, because of cumsum()). 
Now we can simply compute the scores s for each board after each round and find each board's winning 
round w using argmax(). Finally, we print the scores of the first and last winner.
'''

from numpy import loadtxt

n, *b = open('input.txt')
n = loadtxt(n.split(',')).reshape(-1,1,1,1)    # (numbers,1,1,1)
b = loadtxt(b).reshape(1,-1,5,5)               # (1,boards,5,5)

m = (n == b).cumsum(0)                         # (numbers,boards,5,5)
s = (n * b * (1-m)).sum((2,3))                 # (numbers,boards)
w = (m.all(2) | m.all(3)).any(2).argmax(0)     # (boards,)

print(s[w].diagonal()[w.argsort()[[0,-1]]])