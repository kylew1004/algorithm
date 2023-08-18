# https://www.acmicpc.net/problem/2437

import sys
input = sys.stdin.readline

n = int(input())
weight = list(map(int, input().split()))
weight.sort()
answer = 1

for w in weight:
    if answer < w:
        break
    answer += w

print(answer)
