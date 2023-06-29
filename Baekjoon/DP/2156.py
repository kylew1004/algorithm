# https://www.acmicpc.net/problem/2156

import sys
input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]
answer = [0 for _ in range(n)]

if n >= 1:
    answer[0] = wines[0]
if n >= 2:
    answer[1] = wines[0] + wines[1]
if n >= 3:
    answer[2] = max(wines[0] + wines[1], wines[0] + wines[2], wines[1] + wines[2])
if n > 3:
    for i in range(3, n):
        answer[i] = max(answer[i - 1], answer[i - 2] + wines[i], answer[i - 3] + wines[i - 1] + wines[i])

print(answer[-1])