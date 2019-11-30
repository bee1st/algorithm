import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0] + x[1] + x[2]
b = a % 10

if b == 0 :
    print('운수대통!')

else :
    print('노력하세요!')