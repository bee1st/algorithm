import sys
jumsu = int(input())
x = list(map(int, sys.stdin.readline().split()))

count = 0

for i in range(jumsu):
    if x[i] == 1 :
        if i > 0 and x[i - 1] >= 1:
            x[i] =  x[i - 1] + 1
        else:
            x[i] = 1

for i in range(jumsu):
    count += x[i]

print(count)

