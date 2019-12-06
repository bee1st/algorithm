import sys
x = list(map(int, sys.stdin.readline().split()))

y = x[0]
m = x[1]

if y % 4 == 0 and m == 2:
    print('29')

elif y % 4 != 0 and m == 2:
    print('28')

elif m == 4 or m == 6 or m == 9 or m == 11 :
    print('30')

else :
    print('31')
