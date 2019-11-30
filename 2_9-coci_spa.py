import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = ((a * 60) + b - 45)
d = (c // 60)
e = (c % 60)

print(d, e)
