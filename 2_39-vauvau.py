a1, b1, a2, b2 = map(int, input().split())
p, m, g = map(int, input().split())

a = p % (a1 + b1)
b = m % (a1 + b1)
c = g % (a1 + b1)

d = p % (a2 + b2)
e = m % (a2 + b2)
f = g % (a2 + b2)

if 0 < a <= a1 and 0 < d <= a2:
    print('both')

elif 0 < a <= a1 or 0 < d <= a2:
    print('one')

else : 
    print('none')


if 0 < b <= a1 and 0 < e <= a2:
    print('both')

elif 0 < b <= a1 or 0 < e <= a2:
    print('one')

else : 
    print('none')


if 0 < c <= a1 and 0 < f <= a2:
    print('both')

elif 0 < c <= a1 or 0 < f <= a2:
    print('one')

else : 
    print('none')