a, b, c, d, e, f, g = map(int, input().split())

x = [a, b, c, d, e, f, g]

i=0
j=0
k=100

for i in x:
    if i % 2 == 1:
        j = j + i
        if k > i:
            k = i

if j == 0:
    print('-1')
else:
    print(j)
    print(k)        

