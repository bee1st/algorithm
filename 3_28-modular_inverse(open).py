x , m = map(int, input().split())

n = 0

for n in range(0, 100):
    n = n + 1
    if (x * n) % m == 1:
        print(n)
        break

if (x * n) % m != 1:
    print('No such integer exists.')