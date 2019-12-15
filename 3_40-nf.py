# import sys
# x = list(map(int, sys.stdin.readline().split()))

# a = x[0]

# for i in range(0, 10000):
#     i = i + 1
#     if a % i == 0 and 0 < i <= a: 
#         if i**2 == a and a % i == 0:
#             print('yes')
#         elif i**2 != a and a % i == 0:
#             print('no')
    
import sys
x = list(map(int, sys.stdin.readline().split()))
a = x[0]

import math

if int(math.sqrt(a)) == math.sqrt(a):
    print('yes')
else :
    print('no')