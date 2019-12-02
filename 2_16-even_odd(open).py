import sys
x = list(map(int, sys.stdin.readline().split()))

# odd even

a = x[0] % 2
b = x[1] % 2

if a == 0 and b == 0:
    print('even+even=even')
    print('even*even=even')

elif a == 0 and b == 1:
    print('even+odd=odd')
    print('even*odd=even')

elif a == 1 and b == 0:
    print('odd+even=odd')
    print('odd*even=even')

elif a == 1 and b == 1:
    print('odd+odd=even')
    print('odd*odd=odd')
