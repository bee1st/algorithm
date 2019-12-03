x1, y1 = input().split()
x2, y2 = input().split()
x3, y3 = input().split()

a = [x1, x2, x3]
b = [y1, y2, y3]

a.sort()
b.sort()

if a[0] == a[1] and b[0] == b[1] :
    print(a[2], b[2])

elif a[0] != a[1] and b[0] == b[1] :
    print(a[0], b[2])

elif a[0] == a[1] and b[0] != b[1]:
    print(a[2], b[0])

elif a[0] != a[1] and b[0] != b[1] :
    print(a[0], b[0])