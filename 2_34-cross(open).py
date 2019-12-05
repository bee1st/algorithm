a, b = map(int, input().split())
c, d = map(int, input().split())

if a < c < b:
    if 1 <= d < a or 100 >= d > b:
        print('cross') 
    else:
        print('not cross')
elif a < d < b:
    if 1 <= c < a or 100 >= c > b:
        print('cross')
    else:
        print('not cross')

elif b < c < a:
    if 1 <= d < b or 100 >= d > a:
        print('cross')
    else:
        print('not cross')

elif b < d < a:
    if 1 <= c < b or 100 >= c > a:
        print('cross')
    else:
        print('not cross')

else :
    print('not cross')