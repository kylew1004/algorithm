# https://atcoder.jp/contests/abc330/tasks/abc330_a

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
s = list(map(int, input().split()))
answer = 0

for i in range(n):
    if s[i] >= l:
        answer += 1

print(answer)