import sys
x = list(map(int, sys.stdin.readline().split()))

a = (x[0], x[1], x[2])
b = (x[2] - x[1] -1)
c = (x[1] - x[0] -1)

if b >= c :
    print(b)

elif b < c :
    print(c)