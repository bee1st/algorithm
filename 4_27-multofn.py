import sys
x = list(map(int, sys.stdin.readline().split()))

n = x[0]
count = 0

for a in range(1, 3 + 1):
    a = 1000 * a
    for b in range(1, 3 + 1):
        b = 100 * b
        for c in range(1, 3 + 1):
            c = 10 * c
            for d in range(1, 3 + 1):
                d = 1 * d
                if (a + b + c + d) % n == 0:
                    count += 1

print(count)