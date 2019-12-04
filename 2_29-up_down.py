a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

n = (s // (a + b)) * (a - b) + s % (a + b)
m = (s // (c + d)) * (c - d) + s % (c + d)

if n > m or (s == a and a > c):
    print('Nikky')

elif n < m or (s == c and c > a):
    print('Byron')

elif n == m :
    print('Tied')