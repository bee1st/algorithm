import sys
x = list(map(int, sys.stdin.readline().split()))

b = x[0]
d = x[1]
s = x[2]
D = x[3]

b_0 = [461, 431, 420, 0]
d_0 = [130, 160, 118, 0]
s_0 = [100, 57, 70, 0]
D_0 = [167, 266, 75, 0]

z = b_0[b - 1] + d_0[d - 1] + s_0[s - 1] + D_0[D - 1]

print(f'Your total Calorie count is {z}.')
