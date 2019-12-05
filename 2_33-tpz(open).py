a = int(input())
b, c, d = map(int, input().split())

e = [b, c, d]
e.sort()

f = e[0] - ((a - e[2]) + (a - e[1]))

if f > 0 :
    print(e[0], f)

elif f <= 0 :
    print(e[0], 0)