import sys
x = list(map(int, sys.stdin.readline().split()))

n = (x[0] * (x[0]-1)) / 2

print(int(n))