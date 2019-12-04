import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = (a + b) % 2

if a >= b and c == 0 :
    s = (a + b) / 2
    d = s - b
    print(int(s), int(d))

else :
    print('impossible')