import sys
x = list(map(int, sys.stdin.readline().split()))

# a/b 와 c/d 의 대소판별
# a/b > c/d 이면 1
# a/b = c/d 이면 0
# a/b < c/d 이면 -1

# 입력 a, b, c, d

a = x[0]
b = x[1]
c = x[2]
d = x[3]

if a/b > c/d :
    print('1')

elif a/b == c/d :
    print('0')

elif a/b < c/d :
    print('-1')