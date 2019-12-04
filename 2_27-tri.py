import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = x[2]

y = [a, b, c]
y.sort()

if y[0] + y[1] > y[2] :
    print('yes')

else :
    print('no')