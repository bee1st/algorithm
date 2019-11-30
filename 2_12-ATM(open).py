import sys
x = list(map(float, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = a % 5
d = a % 10

if a < (b - 0.5):
    if c == 5 or d == 0 :
        e = b - a - 0.5
        print(f'{e:.2f}')
    
    elif c != 5 or d != 0 :
        print(f'{b:.2f}')

elif a == (b - 0.5):
    f = b - a - 0.5
    print(f'{f:.2f}')

else :
    print(f'{b:.2f}')
