# https://www.acmicpc.net/problem/1758

import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse = True)
result = 0

for i in range(n):
    if arr[i] - i > 0:
        result += arr[i] - i

print(result)
