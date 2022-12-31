# https://www.acmicpc.net/problem/2012

import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()

diff = 0
for i in range(1, n + 1):
    diff += abs(i - nums[i - 1])

print(diff)
