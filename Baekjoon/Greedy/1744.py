# https://www.acmicpc.net/problem/1744

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
plus = []
minus = []

for num in arr:
    if num > 0:
        plus.append(num)
    else:
        minus.append(num)

plus.sort(reverse=True)
minus.sort()
ans = 0

for i in range(0, len(plus), 2):
    if i + 1 < len(plus):
        ans += max(plus[i] * plus[i + 1], plus[i] + plus[i + 1])
    else:
        ans += plus[i]

for i in range(0, len(minus), 2):
    if i + 1 < len(minus):
        ans += minus[i] * minus[i + 1]
    else:
        ans += minus[i]
        
print(ans)
