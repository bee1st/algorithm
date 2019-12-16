import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = x[2]

d = [a, b, c]
d.sort()

i = d[0]
j = d[1]
k = d[2]

for y in range(-100, 201):
    if i < y < k:
        if k - j == j - i == i - y or k - j == j - y == y - i or k - y == y - j == j - i :
            print(y)
    elif y > k:
        if y - k == k - j == j - i:
            print(y)
