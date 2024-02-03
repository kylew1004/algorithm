# https://www.acmicpc.net/problem/3003

import sys
input = sys.stdin.readline

chess = list(map(int, input().split()))
standard = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(standard[i] - chess[i], end=' ')