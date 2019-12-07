a, b, c, d, e, f, g = map(int, input().split())

x = [a, b, c, d, e, f, g]

y = max(x)


for i , j in enumerate(x):
    if j == y:
        print(i+1)