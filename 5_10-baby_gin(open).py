import sys
x = list(map(int, sys.stdin.readline().split()))
  
x.sort()
  
if x[0] == x[1] == x[2]:
    if x[3] == x[4] == x[5]:
        print('gin')
    elif x[3] + 2 == x[4] + 1 == x[5]:
        print('gin')
    else:
        print('lose')
  
elif x[0] + 2 == x[1] + 1 == x[2]:
    if x[3] == x[4] == x[5]:
        print('gin')
    elif x[3] + 2 == x[4] + 1 == x[5]:
        print('gin')
    else:
        print('lose')
 
elif x[0] + 1 == x[1] and x[4] + 1 == x[5]:
    if x[0] + 2 == x[2] + 1 == x[5]:
        if x[1] == x[3] == x[4]:
            print('gin')
        else:
            print('lose')
 
    elif x[0] + 2 == x[2] + 1 == x[3]:
        if x[1] + 2 == x[4] + 1 == x[5]:
            print('gin')
        else:
            print('lose')
             
    else:
        print('lose')
 
elif x[0] == x[1] and x[2] == x[3] and x[4] == x[5]:
    if x[0] + 2 == x[2] + 1 == x[4] and x[1] + 2 == x[3] + 1 == x[5]:
        print('gin')
    else:
        print('lose')
  
else:
    print('lose')