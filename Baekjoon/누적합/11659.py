# https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
idx_total = [0]
total = 0

for idx in range(n):
    total += nums[idx]
    idx_total.append(total)


for _ in range(m):
    i, j = map(int, input().split())
    print(idx_total[j] - idx_total[i - 1])
