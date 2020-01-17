import sys
x = list(map(int ,sys.stdin.readline().split()))

n = x[0]

for i in range(1, 6 + 1):
    for j in range(i, 6 + 1):
        if i + j == n:
            print(i, j)
