# https://www.acmicpc.net/problem/2442

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))