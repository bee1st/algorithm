a, b, c, d, e, f, g = map(int, input().split())

x = [a, b, c, d, e, f, g]

y = 0
z = 0
q = 0

for i in x:
    if i < 10:
        y = i + y
    elif 10 <= i < 100 :
        z = i + z
    elif i >= 100:
        q = i + q
print(y, z, q)