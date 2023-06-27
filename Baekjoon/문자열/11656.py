# https://www.acmicpc.net/problem/11656

import sys
input = sys.stdin.readline

s = input().rstrip()
arr = [s[i:] for i in range(len(s))]
arr.sort()

for i in range(len(arr)):
    print(arr[i])