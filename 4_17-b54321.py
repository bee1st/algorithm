import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]

for i in range(1, n + 1):
    for j in range(n + 1, 1, -1):
        if j - i > 0:
            print(j - i, end='')

    print(sep='\n')
    print(' ' * i, end='')
    