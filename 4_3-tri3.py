import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]

for i in range(0, a):
    for j in range(i):
        print(' ', end='')
    for j in range(a - i):
        print('*', end='')
    print(sep='\n')