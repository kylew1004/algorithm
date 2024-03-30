# https://www.acmicpc.net/problem/2920

import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

if arr == sorted(arr):
    print("ascending")
elif arr == sorted(arr, reverse=True):
    print("descending")
else:
    print("mixed")