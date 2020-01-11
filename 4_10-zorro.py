import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]

for i in range(1, n + 1):
    for j in range(0, n):
        if i == 1 :
            print('*', end='')
        elif i == n:
            print('*', end='')
    if 1 < i < n:
        print(' ' * (n - i), end='')
        print('*' * 1, end='')
    print(sep='\n')
