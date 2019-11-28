import sys
x = list(map(float, sys.stdin.readline().split()))

a = int((x[0] * 100) // 100)
b = ((x[0] * 100) % 100) / 100

print(f'{a} {b:.2f}')