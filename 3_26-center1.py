a = int(input())

j = 0
y = 0

for i in range(0, a - 1):
    i = i + 1
    j = j + i

for x in range(a, 10000):
    x = x + 1
    y = y + x
    if j < y:
        print('X')
        break
    elif j == y :
        print('O')
        break