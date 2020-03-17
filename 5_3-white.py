import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = x[2]
d = x[3]
e = x[4]
f = x[5]

g = [1, 1, 2, 2, 2, 8]

print(g[0] - a, g[1] - b, g[2] - c, g[3] - d, g[4] - e, g[5] - f)