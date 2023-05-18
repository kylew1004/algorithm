# https://www.acmicpc.net/problem/1052
# 0을 세면 시간초과가 난다.

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0

while bin(n).count('1') > k:
    cnt += 1
    n += 1

print(cnt)