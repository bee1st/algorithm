import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]
b = 0

for i in range(0, 301):
    i = i + 1
    a = (i**2) + i
    if a >= (2 * n) :
        break

for j in range(0, i + 1):
    b = b + i - j
    if b < n:
        c = n - b

print(i, c)