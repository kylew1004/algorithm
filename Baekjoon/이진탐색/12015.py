# https://www.acmicpc.net/problem/12015

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0]

for i in range(n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
    else:
        start, end = 0, len(dp)
        while start < end:
            mid = (start + end) // 2
            if dp[mid] < arr[i]:
                start = mid + 1
            else:
                end = mid
        dp[end] = arr[i]

print(len(dp) - 1)