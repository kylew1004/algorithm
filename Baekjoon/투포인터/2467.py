# https://www.acmicpc.net/problem/2467

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
left, right = 0, n - 1
result = [arr[left], arr[right]]
min_value = abs(arr[left] + arr[right])

while left < right:
    total = arr[left] + arr[right]
    if abs(total) < min_value:
        min_value = abs(total)
        result = [arr[left], arr[right]]
    if total < 0:
        left += 1
    elif total > 0:
        right -= 1
    else:
        break

print(result[0], result[1])