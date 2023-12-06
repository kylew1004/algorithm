# https://www.acmicpc.net/problem/23505

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

arr.sort(reverse=True)
print(arr[k - 1])