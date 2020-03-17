import sys
n = int(input())
x = list(map(int, sys.stdin.readline().split()))

a = 0
sum = 0
v = 0

for i in range(n):
    sum = sum + x[i]

Avg = sum / n

for k in range(n):
    v = v + ((x[k] - Avg) ** 2)

a = v / n

print(f'{a:.2f}')


