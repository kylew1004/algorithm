# https://www.acmicpc.net/problem/14425

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set(input() for _ in range(n))
cnt = 0

for _ in range(m):
    ts = input()
    if ts in s:
        cnt += 1

print(cnt)
