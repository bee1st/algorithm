import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]


if (a % 2 == 0 and b % 2 == 0) and (a == b or a != b) and (a - b == 0 or a - b == 2):
    print(a + b)
elif (a % 2 == 1 and b % 2 == 1) and (a - b == 2 or a - b == 0):
    print(a + b - 1)
else:
    print('No Number')