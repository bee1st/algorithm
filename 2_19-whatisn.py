import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]

if a <= 5:
    print((a//2) +1)

else :
    print((a//2) - (a-6))