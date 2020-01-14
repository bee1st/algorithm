import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]
a = 0
b = 0
for i in range(1, n + 1):
    a = a + i
    b = b + a
print(b)