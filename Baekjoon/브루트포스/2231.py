# https://www.acmicpc.net/problem/2231

import sys
input = sys.stdin.readline

n = int(input())
ans = 0

for i in range(1, n+1):
    tmp = i
    for j in str(i):
        tmp += int(j)
    if tmp == n:
        ans = i
        break

print(ans)
