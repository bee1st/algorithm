import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]
m = (n + 1) // 2

for i in range(1, n + 1):
    for j in range(0, n - 1):
        if i == 1 :
            print('*', end='')
        elif i == m:
            print('*', end='')
    print('*', sep='\n')
