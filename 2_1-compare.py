import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]

if a > b :
    print('>')

elif a == b :
    print('=')

elif a < b :
    print('<')