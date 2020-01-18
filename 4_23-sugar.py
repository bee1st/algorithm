import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]
a = 0
b = 0
c = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if 5 * i + 3 * j == n:
            a = i + j
            
if n % 5 == 0:
    b = n // 5
elif n % 3 == 0:
    c = n // 3


if n == 4 or n == 7:
    print('-1')
     
elif a == 0 and b == 0:
    print(c)
elif b == 0 and c == 0:
    print(a)
elif c == 0 and a == 0:
    print(b)
elif a == 0:
    if b < c:
        print(b)
    elif c < b:
        print(c)
elif b == 0:
    if a < c:
        print(a)
    elif c < a:
        print(c)
elif c == 0:
    if b < a:
        print(b)
    elif a < b:
        print(a)