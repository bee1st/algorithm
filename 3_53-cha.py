import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = 0
print(a, b, end=' ')
while True:
    c = a - b
    a = b
    b = c
    if c < 0:
        break
    print(c, end=' ')