# https://www.acmicpc.net/problem/2343

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = max(arr)
right = sum(arr)

while left <= right:
    mid = (left + right) // 2
    cnt = 1
    tmp = 0

    for i in arr:
        if tmp + i > mid:
            cnt += 1
            tmp = 0
        tmp += i

    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1

print(left)