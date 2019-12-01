import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = (a - 2000) % 8


if a >= 2000 and b == 0 :
    print('O')

else :
    print('X')
