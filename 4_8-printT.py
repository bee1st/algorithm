import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]
m = (n + 1) // 2

for i in range(1, n + 1):
    for j in range(n):
        if i == 1:
            print('*', end='')
    if 1 < i:
        print(' ' * (m - 1), end='')
        print('*', end='')
    
    print(sep='\n')