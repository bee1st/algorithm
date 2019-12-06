x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

if (x3 <= (x1 or x2) <= x4) and (y3 <= (y1 or y2) <= y4):
    print('Overlap')

elif (x1 <= (x3 or x4) <= x2) and (y1 <= (y3 or y4) <= y2):
    print('Overlap')

elif (x3 <= (x1 or x2) <= x4) and (y1 <= (y3 or y4) <= y2):
    print('Overlap')

elif (x1 <= (x3 or x4) <= x2) and (y3 <= (y1 or y2) <= y4):
    print('Overlap')

else :
    print('No overlap')
