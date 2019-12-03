x1, y1 = input().split()
x2, y2 = input().split()

x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

a = ((x1 / x2) + (y1 / y2))
b = ((x2 / y2) + (x1 / y1))
c = ((y2 / y1) + (x2 / x1))
d = ((y1 / x1) + (y2 / x2))

if a < b < c < d or b < c < a < d or c < b < a < d or b < a < c < d or c < a < b < d :
    print('3')

elif a < b < c and a < c :
    print('2')

elif a < b :
    print('1')

else :
    print('0')