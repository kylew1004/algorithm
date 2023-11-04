# https://www.acmicpc.net/problem/2501

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0

for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
if cnt < k:
    print(0)