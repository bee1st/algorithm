import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]

for i in range(n):
    for j in range(n, 0, -1):
        if j - i > 0:
            print(j - i, end='')
    print(sep='\n')
