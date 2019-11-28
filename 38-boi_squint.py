import math
import sys
x = list(map(int,sys.stdin.readline().split()))

y = math.sqrt(x[0])
z = math.ceil(y)

print(z)