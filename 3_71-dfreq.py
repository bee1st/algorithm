import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]
m = x[1]
count = 0

for i in range(0, n + 1):
    for j in range(0, 10):
        j = 10**j
        if j < n:
            if (i // j) % 10 == m or i == m * j:
                count = count + 1


print(count)

pass 
# 시간초과