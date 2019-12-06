import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = x[2]

p = a + (a * (b / 100))  #정가 
s = p - (p * (c / 100))  #할인가
z = s - a

if z < 0 :
    print('loss')

elif z >= 0 :
    print(f'{z:.0f}')