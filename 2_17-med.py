import sys
x = list(map(int, sys.stdin.readline().split()))

a = [x[0], x[1], x[2]]
a.sort()
print(a[1])