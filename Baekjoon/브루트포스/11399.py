# https://www.acmicpc.net/problem/11399

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(" ")))
result = 0
arr.sort()

for i in range(n):
    for j in range(i + 1):
        result += arr[j]
print(result)