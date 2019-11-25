a, b = input().split()
c, d = input().split()

x = int(a)
y = int(b)
z = int(c)
f = int(d)
g = int((f-y)/(z-x))

print(g, f - (g * z))

