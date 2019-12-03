import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0] % 2
b = x[1] % 2

if a == 1 and b == 1 :
    print('white')

elif a == 1 and b == 0 :
    print('black')

elif a == 0 and b == 1 :
    print('white')

elif a == 0 and b == 0 :
    print('black')
