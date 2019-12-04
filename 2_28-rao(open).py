import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = x[2]

y = [a, b, c]
y.sort()

m = (y[0] ** 2) + (y[1] ** 2)
n = (y[2] ** 2)

if m == n:
    print('right')

elif m > n:
    print('acute')

elif m < n:
    print('obtuse')