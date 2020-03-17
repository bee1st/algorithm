import sys
x = list(map(int, sys.stdin.readline().split()))


x.sort()
x.reverse()

print(x[0] + x[1])
print(x[0], x[1])