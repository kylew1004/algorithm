# https://www.acmicpc.net/problem/20115

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
res = arr[0]

for i in range(1, len(arr)):
    res += arr[i] / 2

print(res)