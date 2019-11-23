import sys
x = list(map(int, sys.stdin.readline().split()))

D = int(input())

x_1 = (x[0] * 3600) + (x[1] * 60) + x[2] + D

a = (x_1 / 3600) % 24
a_1 = x_1 % 3600
b = a_1 / 60
b_1 = a_1 % 60
c = b_1 % 60

print(f'{int(a)} {int(b)} {int(c)}')
