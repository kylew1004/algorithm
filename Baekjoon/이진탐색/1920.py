# https://www.acmicpc.net/problem/1920

import sys

input = sys.stdin.readline

def binary_search(i, N, start, end):
    if start > end:
        return 0
    
    mid = (end+start) // 2
    if i == N[mid]:
        return 1
    elif i < N[mid]:
            return binary_search(i, N, start, mid-1)
    else:
        return binary_search(i, N, mid+1, end)

n = int(input())
cnt = 0

N = list(map(int, input().split()))
N.sort()

m = int(input())
M = list(map(int, input().split()))

for i in M:
    print(binary_search(i, N, 0, len(N) - 1))