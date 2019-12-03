import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = x[2]
d = x[3]

if (a - c) == 0 and (d - b) == 0:
    print('many')

elif (a - c) == 0 or (d - b) == 0:
    print('none')

elif (a - c) != 0 and (d - b) != 0:
    e = ((d - b) / (a - c))
    print(f'{e:.3f}')