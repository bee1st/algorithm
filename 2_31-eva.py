import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = x[2]
d = x[3]

if (c - b) == (d - c) :
    e = d + (d - c)
    print(a, b, c, d, int(e))

elif (c / b) == (d / c) :
    e = d * (d / c)
    print(a, b, c, d, int(e))