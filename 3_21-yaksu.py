a, b = map(int, input().split())
c = 0
count = 0

for i in range(0, a+1):
    i = i + 1
    if a % i == 0:
        count += 1
        if count == b:
            print(i)

if count < b:
    print('0')
            