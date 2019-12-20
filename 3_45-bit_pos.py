n = int(input())
pos = 0
while n:
    if n % 2:
        print(pos, end=' ')
    pos = pos + 1
    n = n // 2