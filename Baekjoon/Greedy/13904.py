# https://www.acmicpc.net/problem/13904

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
day = [0] * 1001
arr.sort(key = lambda x: x[1], reverse = True)

for i in range(n):
    for j in range(arr[i][0], 0, -1):
        if day[j] == 0:
            day[j] = arr[i][1]
            break

print(sum(day))
