# https://www.acmicpc.net/problem/11497

import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    level = 0
    for j in range(2, n):
        level = max(level, abs(nums[j] - nums[j - 2]))
    print(level)