import sys
x = list(map(int, sys.stdin.readline().split()))

e = x[0]
f = (e + 1) // 2

for i in range(1, e + 1):
    for j in range(0, e):
        if i == 1:
            print('*', end='')
        elif i == f:
            print('*', end='')
        elif i == e:
            print('*', end='')
    if 1 < i < f:
        print(' ' * (e -1), end='')
        print('*', end='')
    elif f < i < e:
        print(' ' * (e -1), end='')
        print('*', end='')
    print(sep='\n')
    

