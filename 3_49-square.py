M = int(input())
N = int(input())

min = 100000
sum = 0

for i in range(0, 101):
    square = i * i
    if M <= square <= N:
        if min >= square:
            min = square
        sum = sum + square

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)