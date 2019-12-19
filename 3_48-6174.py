import sys
x = list(map(int, sys.stdin.readline().split()))

z = x[0]
a = 0
for i in range(1, 5):
    i = (z % 10**i) // 10**(i - 1)
    a = i

    # b = (a[3] * 1000) + (a[2] * 100) + (a[1] * 10) + a[3]
    # c = (a[0] * 1000) + (a[1] * 100) + a([2] * 10) + a[0]
    # if b - c == 6174:
    #     print()

pass
