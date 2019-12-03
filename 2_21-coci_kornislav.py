import sys
x = list(map(int, sys.stdin.readline().split()))

a = [x[0], x[1], x[2], x[3]]
a.sort()

b = (a[0] * a[2])

print(b)