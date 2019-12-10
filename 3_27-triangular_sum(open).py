import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
j = 0
k = 0

for i in range(0, a):
    i = i + 1
    j = j + i
    k = k + i * (1 + i + j)
    
print(k)