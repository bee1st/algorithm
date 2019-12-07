import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]

c = [a, b]
c.sort()

d = c[0]

for d in range(c[0] -1, c[1], 1):
    d = d + 1
    if d <= c[1]:
        print(d, end=' ')