# https://www.acmicpc.net/problem/11404

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
print(nums[k - 1])