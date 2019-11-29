import sys
x = list(map(int, sys.stdin.readline().split()))

print(f'{x[0]}+{x[1]}={x[0]+x[1]}')
print(f'{x[0]}-{x[1]}={x[0]-x[1]}')
print(f'{x[0]}*{x[1]}={x[0]*x[1]}')
print(f'{x[0]}/{x[1]}={x[0]//x[1]}')
print(f'{x[0]}%{x[1]}={x[0]%x[1]}')