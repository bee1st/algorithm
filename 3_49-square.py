a = int(input())
b = int(input())
c = 0

for i in range(0, 101):
    i = i * i
    if a <= i <= b:
        c = c + i
        d = i
        if d == c:
            print(c)

pass

