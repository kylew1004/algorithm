# https://www.acmicpc.net/problem/14487

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = 0

for i in arr:
    result += i
result -= max(arr)

print(result)