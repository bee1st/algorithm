import sys
x = list(map(int, sys.stdin.readline().split()))

import math

a = (x[0] // 2) + (x[0] % 2)
b = math.ceil(x[0] / 3)

print(a, b)

