import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]

for i in range(1, n + 1):
    for j in range(1, 10 + 1):
        j = i ** j
        print(' ' )

pass
