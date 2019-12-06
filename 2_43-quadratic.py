import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = x[2]

y = (b**2) - (4 * a * c)
z = (-b + y**0.5) / (2 * a)
z1 = (-b - y**0.5) / (2 * a)


if y > 0 :
    d = [z, z1]
    d.sort()
    print('2')
    print(f'{d[0]:.3f} {d[1]:.3f}')

elif y == 0 :
    d = -b / (2 * a)
    print('1')
    print(f'{d:.3f}')

elif y < 0:
    print('0')
   
    


