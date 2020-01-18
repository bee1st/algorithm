import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]
a = 0
b = 0
c = 0

if 3 <= n < 5000:
    if n % 5 == 0:
        b = n // 5
    elif n % 3 == 0:
        c = n // 3
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if 5 * i + 3 * j == n:
                a = i + j

if a == 0:
    if b == 0:
        print(c)
    elif c == 0:
        print(b)
elif a != 0:
    if a < b:
        print(a)
    elif a < c:
        print(a)
    elif b < a:
        print(b)
    elif c < a:
        print(c)
    elif b < c:
        print(b)
    elif c < b:
        print(c)
else:
    print('-1')

pass

