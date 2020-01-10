import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]

for i in range(1, a + 1):
    for j in range(a + 1 - i):
        print('*', end='')
    print(sep='\n')