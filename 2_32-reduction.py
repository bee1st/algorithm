import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1] 
c = x[2]  
d = x[3] 

e = c / a
f = d / a
g = c / b
h = d / b

round(e, 2)
round(f, 2)
round(g, 2)
round(h, 2)

e = int(e * 100)
f = int(f * 100)
g = int(g * 100)
h = int(h * 100)

y = [e, f, g, h]
y.sort()

if y[1] < 100 and ((a + b) > (c + d)):
    print(f'{y[1]}%')

elif y[1] < 100 and ((a + b) < (c + d)) : 
    print(f'{y[1]}%')

else : 
    print(f'100%')