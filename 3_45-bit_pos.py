import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]

while a // 2 > 0:
    print(a % 2)
    a = a // 2
    continue

print(a % 2)

# pass