import sys
x = list(map(int, sys.stdin.readline().split()))

r = x[0]
e = x[1]
c = x[2]

if r < e - c :
    print('advertise')

elif r > e - c :
    print('do not advertise')

else :
    print('does not matter')