import sys
x = list(map(float, sys.stdin.readline().split()))

w = x[0]
l = x[1]

for i in range(0, 1000000):
    i = i + 1
    if w % i == 0 and l % i == 0:
        a = (w // i) * (l // i)

print(int(a))
