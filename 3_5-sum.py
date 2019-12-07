a, b, c, d, e, f, g = map(int, input().split())

x = [a, b, c, d, e, f, g]

y = 0

for i in x:
    y = i + y

print(y)