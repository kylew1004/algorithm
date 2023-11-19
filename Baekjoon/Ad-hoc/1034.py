# https://www.acmicpc.net/problem/1034

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
k = int(input())

result = 0
for i in range(n):
    zero_count = arr[i].count('0')
    if zero_count <= k and zero_count % 2 == k % 2:
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        result = max(result, count)

print(result)