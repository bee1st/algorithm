a = int(input())
b = 0

for i in range(0, a+1):
    i = i + 1
    if a % i == 0:
        b += 1
        
print(b)