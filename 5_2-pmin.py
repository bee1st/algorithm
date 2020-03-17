import sys
a = int(input())
b = list(map(int, sys.stdin.readline().split()))

b.index(min(b))

for i, j in enumerate(b):
    if j == min(b):
        print(i + 1, end=' ')
