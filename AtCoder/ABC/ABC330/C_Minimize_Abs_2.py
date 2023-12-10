# https://atcoder.jp/contests/abc330/tasks/abc330_c

import sys
input = sys.stdin.readline

D = int(input())
min_diff = float('inf')

for x in range(int(D ** 0.5) + 1):
    y = int((D - x ** 2)**0.5)
    diff = abs(x ** 2 + y ** 2 - D)

    if y + 1 <= int(D ** 0.5) + 1:
        diff_next_y = abs(x ** 2 + (y + 1) ** 2 - D)
        if diff_next_y < diff:
            diff = diff_next_y
            y += 1

    if diff < min_diff:
        min_diff = diff

print(min_diff)