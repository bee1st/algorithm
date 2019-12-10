a = int(input())
b = 0

for i in range(0, a+1):
    i = i + 1
    if a % i == 0:
        b = b + i

c = b - a

if c == a :
    print('{:>5}'.format(a), 'PERFECT', sep='  ')

elif c > a :
    print('{:>5}'.format(a), 'ABUNDANT', sep='  ')

else:
    print('{:>5}'.format(a), 'DEFICIENT', sep='  ')