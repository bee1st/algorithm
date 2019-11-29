import sys
x = list(map(int, sys.stdin.readline().split()))

k = x[0]
n = x[1]

h = (n-1) / (k-1) * 100

print(int(h))
