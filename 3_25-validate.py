import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = x[2]
d = x[3]
e = x[4]


z = (a**2 + b**2 + c**2 + d**2 + e**2) % 10

print(z)