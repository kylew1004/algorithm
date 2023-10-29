# https://www.acmicpc.net/problem/14720

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = 0
idx = 0

for i in range(n):
    if arr[i] == idx % 3:
        idx += 1
        result += 1
print(result)