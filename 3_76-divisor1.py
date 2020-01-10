import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
count = 0

for i in range(2, b + 1):
    for j in range(2, b + 1):
        if i % j == 0:
            break

    if i == j :
        j += j
        count = count + 1

for i in range(0, b + 1):
    i = i + 1
    if a < (i * i) < b:
        c = c + (i * i)
        count = count + 1

print(count)
print((c + j) % 1000000003)
    
