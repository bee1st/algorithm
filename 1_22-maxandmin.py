import sys
x = list(map(int, sys.stdin.readline().split()))

print(max(min(x[0],x[1]),x[0]))