import sys
x = list(map(int, sys.stdin.readline().split()))

import math

a = math.floor((x[0] // 8) * (x[1] // 8))
b = (math.ceil(x[0] / 8)) * (math.ceil(x[1] / 8)) - a

print(f'The number of whole tiles is {a} part tiles is {b}')