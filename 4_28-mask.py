import itertools
a = range(10)
for i, j, k, l in itertools.product(a, a, a, a):
    b = 100 * i + 10 * j + l * 2
    c = (100 * i) + (10 * j) + k + (k * 100) + (k * 10) + i
    while b != c:
        break
    else:
        print(b)

pass