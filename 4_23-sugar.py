import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]

if n % 3 == 0:
    print(int(n/3))

elif n % 5 == 0:
    print(int(n/5))

