# https://www.acmicpc.net/problem/10811

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    arr = arr[:i - 1] + arr[i - 1:j][::-1] + arr[j:]
    
print(*arr)