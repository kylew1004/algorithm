# https://www.acmicpc.net/problem/1002

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    if d == 0 and r1 == r2:
        print(-1)
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)
    elif d < r1 + r2 and d > abs(r1 - r2):
        print(2)
    else:
        print(0)