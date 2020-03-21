import sys
n = int(input())
x = list(map(int, sys.stdin.readline().split()))

sum = 0
avg = 0
count = 0
bak = 0

for i in range(n):
    sum = sum + x[i]
    avg = sum / n

for i in range(n):
    if x[i] > avg :
        count += 1

bak = (count / n) * 100
print(f'{bak:.3f}%')


