a = int(input())
i = 0

for x in range(0, a):
    i = x + 1 + i
    print(x+1,end='+')

print(i)
