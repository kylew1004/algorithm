# https://atcoder.jp/contests/arc168/tasks/arc168_a

import sys
input = sys.stdin.readline


N = int(input())
S = input().strip()
answer = 0
count = 0

for char in S:
    if char == '>':
        count += 1
    else:
        answer += count * (count + 1) // 2
        count = 0

answer += count * (count + 1) // 2

print(answer)