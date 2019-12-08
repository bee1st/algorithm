a = int(input())

while True :
    print(a, end=' ')
    if a == 1:
        break
    elif a % 2 == 0:
        a = a // 2
    elif a % 2 != 0:
        a = a * 3 + 1
