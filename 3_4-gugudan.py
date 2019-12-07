import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]

b = 1
c = 0

for b in range(0, 9, 1) :
    b = b + 1
    for c in range(0, 9, 1):
        c = c + 1
        if b == a:
            print(f'{b}*{c}={b*c}')
