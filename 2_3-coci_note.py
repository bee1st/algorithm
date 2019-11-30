import sys
x = list(map(int, sys.stdin.readline().split()))

a = (x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])

b = (1, 2, 3, 4, 5, 6, 7, 8)
c = (8, 7, 6, 5, 4, 3, 2, 1)

if  a == b :
    print('ascending')

elif a == c :
    print('descending')

else:
    print('mixed')

