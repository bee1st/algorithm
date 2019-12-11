
for i in range(0, 10000):
    i = i + 1
    if 0 < i < 10:
        if i == (i**2) % 10:
            print(i)
    elif 10 <= i < 100:
        if i == (i**2) % 100:
            print(i)
    elif 100 <= i < 1000:
        if i == (i**2) % 1000:
            print(i)
    elif 1000 <= i < 10000:
        if i == (i**2) % 10000:
            print(i)
