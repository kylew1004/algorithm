# https://www.acmicpc.net/problem/14215

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
arr = sorted([a, b, c])

if arr[0] + arr[1] > arr[2]:
    print(sum(arr))
else:
    arr[2] = arr[0] + arr[1]
    print(sum(arr) - 1)