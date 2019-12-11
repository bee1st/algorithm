import sys
x = list(map(float, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = x[2]

d = (a * 10**c) // b 

print(d / 10**c)
