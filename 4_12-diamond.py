import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]

for x in range(1, n * 2, 2):
    print((" " * ( (n * 2 - 1 - x) // 2 )) + ("*" * x))

for y in range(n * 2-3, 0, -2):
    print((" " * ( (n * 2 - 1 - y) // 2 )) + ("*" * y))