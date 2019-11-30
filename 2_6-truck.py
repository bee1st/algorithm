import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = x[2]

if a <= 168 :
    print(f'CRASH {a}')

elif b <= 168 :
    print(f'CRASH {b}')

elif c <= 168 :
    print(f'CRASH {c}')

else:
    print('NO CRASH')




