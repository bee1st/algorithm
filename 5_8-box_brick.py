import sys
n = int(input())
x = list(map(int, sys.stdin.readline().split()))

avg = 0
sum = 0
count = 0

for i in range(n):
    sum = sum + x[i]
    avg = sum // n

for i in range(n):
    if x[i] > avg:
        count += x[i] - avg

print("The minimum number of moves is {}.".format(count)) 