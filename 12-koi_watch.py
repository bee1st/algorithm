import sys
x = list(map(int, sys.stdin.readline().split()))

D = int(input())

a = D / 360
a_1 = D % 360
b = a_1 / 60
b_1 = a_1 % 60
c = b_1 % 60

print(f'{x[0]+int(a)} {x[1]+int(b)} {x[2]+c:.0f}')
