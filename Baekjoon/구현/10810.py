# https://www.acmicpc.net/problem/10810

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    arr[i - 1:j] = [k] * (j - i + 1)
    
print(*arr)