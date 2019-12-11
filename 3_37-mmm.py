import sys
x = list(map(int,sys.stdin.readline().split()))

x.sort()

a = sum(x)
b = x[9]
c = x[0]

print(a, b, c)