import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]

for i in range(0, 500000):
    i = i + 1
    for j in range(0, 500000):
        j += 1
        if j % i == 0 and i > 1:
            pass