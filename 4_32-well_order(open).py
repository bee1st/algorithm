count = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if (i < j or j < k) and i != j and j != k and i != k:
                if i + 1 == j:
                    print(i * 100 + j * 10 + k, end=' ')
                    count += 1
                    if count == 5:
                        print(sep='\n')
                        count = 0
                elif j + 1 == k:
                    print(i * 100 + j * 10 + k, end=' ')
                    count += 1
                    if count == 5:
                        print(sep='\n')
                        count = 0