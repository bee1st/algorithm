import sys
x = int(input())
y = list(map(int, sys.stdin.readline().split()))

print(''.join(reversed(y)))