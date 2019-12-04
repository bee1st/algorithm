x1, x2, x3 = map(int, input().split())
y1, y2, y3 = map(int, input().split())

a = x1 / y1
b = x2 / y2
c = x3 / y3

if a < b < c or a < c < b:
    a = x1 - (x1 / y1 * y1)
    b = x2 - (x1 / y1 * y2)
    c = x3 - (x1 / y1 * y3)
    print(f'{a:.6f} {b:.6f} {c:.6f}')

elif b < a < c or b < c < a:
    a = x1 - (x2 / y2 * y1)
    b = x2 - (x2 / y2 * y2)
    c = x3 - (x2 / y2 * y3)
    print(f'{a:.6f} {b:.6f} {c:.6f}')

elif c < a < b or c < b < a:
    a = x1 - (x3 / y3 * y1)
    b = x2 - (x3 / y3 * y2)
    c = x3 - (x3 / y3 * y3)
    print(f'{a:.6f} {b:.6f} {c:.6f}')