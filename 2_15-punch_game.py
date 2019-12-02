import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0] * 10
b = x[1] * 15
c = x[2] * 30
d = x[3] * 40
e = x[4] * 45

h = 100

if a >= h or b >= h or c >= h or d >= h or e >= h:
    print('you win')


# 주먹: 10 데미지
# 날아차기 : 15 데미지
# 아도겐 : 30 데미지
# 연속펀치:40 데미지
# 던지기 : 45 데미지