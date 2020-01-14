import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]
count = 0
for i in range(100):
    for j in range(100):
        if n - i - j == 0:
            count += 1

print(count)


