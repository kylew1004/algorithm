# https://atcoder.jp/contests/abc331/tasks/abc331_a

import sys
input = sys.stdin.readline

mon, day = map(int, input().split())
y, m, d = map(int, input().split())

if m == mon and d == day:
    print(y + 1, 1, 1)
elif d == day:
    print(y, m + 1, 1)
else:
    print(y, m, d + 1)