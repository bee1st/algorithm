import sys
x = list(map(int, sys.stdin.readline().split()))

k = x[0]
b = 1
z = 0

for a in range(0, 1000):
    a = a + 1
    i = (2 * a) - 1
    j = ((2 * k) + (-2 * a) + 1)
    z = z + (i * j)
    if a == k:
        print(z)