# https://www.acmicpc.net/problem/11441

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
sums = [0] * (n + 1)

for i in range(1, n + 1):
    sums[i] = sums[i - 1] + nums[i - 1]

m = int(input())

for _ in range(m):
    i, j = map(int, input().split())
    print(sums[j] - sums[i - 1])