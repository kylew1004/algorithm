# https://www.acmicpc.net/problem/15829

import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().rstrip())
r = 31
cnt = 0

for i in range(n):
    cnt += (ord(arr[i]) - 96) * (r ** i)

print(cnt % 1234567891)
