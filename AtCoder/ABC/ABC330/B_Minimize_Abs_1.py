# https://atcoder.jp/contests/abc330/tasks/abc330_b

import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = list(map(int, input().split()))
answer = []

for a in arr:
    if l <= a <= r:
        num = a
    elif a < l:
        num = l
    else:
        num = r
    answer.append(num)

print(*answer)