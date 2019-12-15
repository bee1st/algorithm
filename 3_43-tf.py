import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]



for i in range(1, 10000, 2):
    for j in range(0, 12):
        if i % 2 == 1:
            if (i * (2**j)) == a:
                print(i, j)
