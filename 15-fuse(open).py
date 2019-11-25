import sys
x = list(map(int, sys.stdin.readline().split()))
import math


a = x[0] * 2.5
b = ((a + (x[1] * 2.0) + (x[2] * 0.5)) * 2) / 10
c = (math.ceil(b)* 10)

print(c , 'amperes')

# 본체 1.5 + 모니터 1.0 = 컴퓨터 2.5
# 프린터 2.0
# 라우터 0.5

# 퓨즈는 두배 견딤, 용량 10배수

# 입력 
# 정수 
# 컴퓨터 프린터 라우터 
# 모든수 100이하
