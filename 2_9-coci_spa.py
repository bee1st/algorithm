# 45분전 시간 출력
# 24시
# 1시간 60분 23시간 = 1380분

import sys
x = list(map(int, sys.stdin.readline().split()))

a = x[0]
b = x[1]
c = ((a * 60) + b - 45)
d = (c // 60)
e = (c % 60)

print(d, e)
