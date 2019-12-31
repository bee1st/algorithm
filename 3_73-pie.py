import sys
x = list(map(int, sys.stdin.readline().split()))
y = list(map(int, sys.stdin.readline().split()))

a = (x[0] * y[1] + x[1] * y[0]) 
b = (x[1] * y[1])
c = b - a

if c == 0:
    print(0)
elif c != 0:
    for i in range(1000, 1, -1):
        i = i - 1
        if c % i == 0 and b % i == 0:
            c = c // i
            b = b // i
    print(f'{c}/{b}')

