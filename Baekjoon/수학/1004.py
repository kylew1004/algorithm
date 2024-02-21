# https://www.acmicpc.net/problem/1004

import sys
input = sys.stdin.readline

def is_in(x, y, cx, cy, r):
    return (x - cx) ** 2 + (y - cy) ** 2 < r ** 2


t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        if is_in(x1, y1, cx, cy, r) ^ is_in(x2, y2, cx, cy, r):
            cnt += 1
    print(cnt)
