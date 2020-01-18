import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]

for i in range(1, n + 1):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if i == sum:
        print(i)