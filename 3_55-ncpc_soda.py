import sys
x = list(map(int, sys.stdin.readline().split()))

e = x[0]
f = x[1]
c = x[2]

k = e + f
a = 0

while True:
    a = a + (k // c)
    k = (k // c) + (k % c)
    if k < c:
        break

print(a)