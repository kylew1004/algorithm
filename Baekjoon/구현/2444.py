# https://www.acmicpc.net/problem/2444

import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))