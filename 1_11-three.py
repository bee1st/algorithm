i = int(input())
j = int(input())

a = i * (j % 10)
print(a)
b = i * ((j % 100) // 10)
print(b)
c = i * (j // 100)
print(c)

print(i * j)

