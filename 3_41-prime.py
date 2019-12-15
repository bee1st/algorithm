import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]

for i in range(0, 30000):
    i = i + 1
    if a % i == 0 and i > 1:
        if a == i:
            print('prime')
        else:
            print('not prime')
            break