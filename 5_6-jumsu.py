import sys
jumsu = int(input())
x = list(map(int, sys.stdin.readline().split()))

count = 0

for i in range(jumsu):
    if x[i] == 1 :
        count += 1
        if x[i] == 1 and x[i + 1] == 1 :
            count += 1
print(count)

