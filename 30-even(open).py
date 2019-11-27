import math
a, b = map(int, input().split())

root_a = math.sqrt(a-1)
root_b = math.sqrt(b)

root_a = int(root_a)
root_b = int(root_b)

odd = (root_b) - (root_a)

print((b-a+1) - odd)