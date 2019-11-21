import sys
x = list(map(int, sys.stdin.readline().split()))

p = 1000-x[0]
a = p // 100
b = (p-(a*100)) // 50
c = (p-(a*100+b*50)) // 10

print(a,b,c)