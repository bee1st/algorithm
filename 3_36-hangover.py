import sys
x = list(map(float,sys.stdin.readline().split()))

a = x[0]
j = 0

for i in range(0, 1000):
    i = i + 1
    j = j + (1 / (i + 1))
    if a <= j:
        break

print(f'{i} card(s)')