import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]
k = x[1]

a = (k * (1 + k)) // 2
count = 0

for i in range(1, n - k + 2):
    i = a + (k * (i - 1))
    if i % 15 == 0:
        count += 1

print(count)