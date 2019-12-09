a = int(input())

i = 0
j = 0

for i in range(0, 100):
    j = i + j
    if j == a:
        print(i)
