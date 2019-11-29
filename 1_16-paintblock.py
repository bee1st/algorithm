import sys
x = list(map(int, sys.stdin.readline().split()))

a = (x[0] - 2)
b = (x[1] - 2)
c = (x[2] - 2)

print((a+b+c) * 4)
