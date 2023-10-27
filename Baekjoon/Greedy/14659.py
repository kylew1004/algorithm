# https://www.acmicpc.net/problem/14659

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = 0
highest = 0

for i in range(n):
    if arr[i] > highest:
        highest = arr[i]
        count = 0
    else:
        count += 1
    answer = max(answer, count)

print(answer)
