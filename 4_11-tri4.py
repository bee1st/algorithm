import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]
m = (n + 1) // 2

for i in range(1, m + 1):
    if i <= n:
        for j in range(m - i):
            print(' ', end='')
        for j in range(2 * i - 1):
            print('*', end='')
    print(sep='\n')
        