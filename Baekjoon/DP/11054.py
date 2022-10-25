# https://www.acmicpc.net/problem/11054

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
buttons = list(input().split())
answer = abs(n - 100)

def check(num):
    nums = list(str(num))
    for i in nums:
        if i in buttons:
            return 0
    return 1

for num in range(1000001):
    if check(num):
        answer = min(answer, len(str(num)) + abs(num - n))

print(answer)
