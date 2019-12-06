import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]

x = 60 * a / 11

if a == 12 :
    print('0.000000')

elif 1 <= a < 11:
    print(f'{x:.6f}')

else :
    print("CAN'T SEE!")
