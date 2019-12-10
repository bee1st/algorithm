a = int(input())
b = 0
count = 0
d = 1

for i in range(0, a+1):
    i = i + 1
    if a % i == 0:
        print(i, end=' ')
        count += 1
        b = b + i
        d = d * i

print()
print(count)
print(b)
print(d % 10)
