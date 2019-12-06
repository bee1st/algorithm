a = int(input())
x1, x2 = map(int, input().split())
y1, y2 = map(int, input().split())

x = abs(x1 - y1)
y = abs(x2 - y2)

if a == 1 :
    print('-1')

elif a >= 2:
    print(x * y)