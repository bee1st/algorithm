import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]

if a == 1 or a == 3 or a == 5 :
    print('enjoy')

else:
    print('oops')