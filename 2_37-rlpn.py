import sys
x = list(map(int, sys.stdin.readline().split()))

x1 = x[0]
y1 = x[1]
x2 = x[2]
y2 = x[3]
x3 = x[4]
y3 = x[5]
x4 = x[6]
y4 = x[7]

if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1 :
    print('none')

elif x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1:
    if ((x1 == x4 or x2 == x3) and (y1 == y4 or y2 == y3)):
        print('point')
    else : 
        print('line')

else : 
    print('rectangle')
