# https://www.acmicpc.net/problem/1041

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print(sum(nums) - max(nums))
else:
    arr = [min(nums[0], nums[5]), min(nums[1], nums[4]), min(nums[2], nums[3])]
    arr.sort()
    total0 = (arr[0] + arr[1]) * (n - 1) * 4
    total1 = (arr[0] + arr[1]) * (n - 2) * 4
    total2 = (arr[0] + arr[1] + arr[2]) * 4
    total3 = arr[0] * (n - 2) * 4
    total4 = arr[0] * (n - 2) * (n - 2) * 5
    print(total0 + total1 + total2 + total3 + total4)