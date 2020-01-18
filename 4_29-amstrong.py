for i in range(100, 1000):
    x = i // 100
    y = (i % 100) // 10
    z = (i % 100) % 10

    j = (x ** 3) + (y ** 3) + (z ** 3)

    if i == j:
        print(i)