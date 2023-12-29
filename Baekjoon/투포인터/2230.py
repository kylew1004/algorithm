# https://www.acmicpc.net/problem/2230

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted([int(input()) for _ in range(n)])

left, right = 0, 0
answer = float('inf')

while left < n and right < n:
    if nums[right] - nums[left] < m:
        right += 1
    else:
        answer = min(answer, nums[right] - nums[left])
        left += 1
        
print(answer)