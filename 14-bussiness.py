import sys
x = list(map(int, sys.stdin.readline().split()))

a = -(x[1] + x[3] - x[2] - x[3] - x[0])

print(a)

# 원가 N
# 정가 M
# 위조 지폐 금액 P
# 거스름돈 C

# N < M , P <= M + C

# M + C - P - C - N
