import sys
x = list(map(int, sys.stdin.readline().split()))

print(int(x[0]) + int(x[0]/4) + int(x[0]/4//4) , int(x[0]%4) + int(x[0]//4%4))