# https://www.acmicpc.net/problem/2559

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, k - 1
result = sum(arr[left:right + 1])
max_value = result

while right < n - 1:
    right += 1
    result += arr[right] - arr[left]
    left += 1
    max_value = max(result, max_value)

print(max_value)
