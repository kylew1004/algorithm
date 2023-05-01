# https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
nums = list(int(input()) for _ in range(k))
start, end = 1, max(nums)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for num in nums:
        lines += num // mid
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)