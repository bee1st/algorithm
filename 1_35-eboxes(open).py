import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]
k = x[1]
t = x[2]
f = x[3]

print(int(n + (f-n) / (k-1) * k))