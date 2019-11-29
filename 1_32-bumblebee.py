import sys
z = list(map(int, sys.stdin.readline().split()))

a = float(z[0])
b = float(z[1])
x = float(z[2])
l = float(z[3])

m = (x * ((l/(a+b))))

print('%.6f' % m)