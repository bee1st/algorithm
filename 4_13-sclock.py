import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]
m = int(n / 2) + 1

for i in range(1, n + 1):
    if i < m:
        print(' ' * (i - 1) + '*' * ((n - 1) - 2 * (i - 1)) + '$')
    elif i > m:
        print(' ' * (m - (i - m) - 1) + '$'+ '*' * (2 * (i - m)))
    else:
        print(' ' * (m - 1) + '$')