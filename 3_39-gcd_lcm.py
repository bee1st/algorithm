import sys
x = list(map(int,sys.stdin.readline().split()))

a = x[0]
b = x[1]

for i in range(0, 1000):
    i = i + 1
    if a % i == 0 and b % i == 0:
        y = i
        z = (i * (a // i) * (b // i))


        
print(y, z)
