# https://www.acmicpc.net/problem/11054
# 1107코드를 잘못 커밋함;;

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
up = [1 for _ in range(n)]
down = [1 for _ in range(n)]
result = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and up[i] < up[j] + 1:
            up[i] = up[j] + 1

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if arr[i] > arr[j] and down[i] < down[j] + 1:
            down[i] = down[j] + 1
    result[i] = down[i] + up[i] - 1

print(max(result))
