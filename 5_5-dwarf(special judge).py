dwarf = []
for i in range(9):
    dwarf.append(int(input()))

q = sum(dwarf)
dwarf.sort()

for i in range(9):
    for j in range(i + 1, 9):
        if q - dwarf[i] - dwarf[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(dwarf[k])
    

    