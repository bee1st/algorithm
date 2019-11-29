import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0] / (60 * 60 * 24)
a_1 = x[0] % (60 * 60 * 24)
b = a_1 / (60 * 60)
b_1 = a_1 % (60 * 60)
c = b_1 / 60
c_1 = b_1 % 60
d = c_1 % 60

print(f'{int(a)} {int(b)} {int(c)} {d:.0f}')