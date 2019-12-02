import sys
x = list(map(float, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = x[2]

if a <= 4.5 and b >= 300 and c>= 500:
    print('Wide Receiver','Lineman','Quarterback')

elif a <= 4.5 and b >= 200 and c >= 300:
    print('Wide Receiver', 'Quarterback')

elif a <= 4.5 and b >= 150 and c >= 200:
    print('Wide Receiver')

elif a <= 5.0 and b >= 200 and c >= 300:
    print('Quarterback')

elif a <= 6.0 and b >= 300 and c >= 500:
    print('Lineman')


else :
    print('No positions')

