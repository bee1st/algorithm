# a = 초항
# d = 공차
# an = 수

# 공식 = (an - a + d ) / d == 0 수열 
#        (an - a + d ) / d != 0 수열 x
import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
d = x[1]
an = x[2]

if (an - a + d) % d == 0:
    print((an - a + d) // d)
else :
    print('X')
    