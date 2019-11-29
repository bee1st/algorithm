import sys
x = list(map(int, sys.stdin.readline().split()))

k = 10**x[1]
a = x[0] / k

print(round(a) * k)