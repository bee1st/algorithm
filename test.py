N = int(input())

N = N - 2

r = N % 2
if r == 1:
  print('7', end='')
else:
  print('1', end='')

q = N // 2
for i in range(q):
  print('1', end='')

print()