import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]

if n % 2 != 0:
    a = (n + 1) // 2
    b = (a - 1) * (a - 1)
    print(b)
elif n % 2 == 0:
    c = n // 2
    d = c * (c - 1)
    print(d)