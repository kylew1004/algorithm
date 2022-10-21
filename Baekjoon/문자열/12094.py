# https://www.acmicpc.net/problem/12904

import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())
answer = 0

while t:
    if t[-1] == "A":
        t.pop()
    elif t[-1] == "B":
        t.pop()
        t = t[::-1]
    if s == t:
        answer = 1
        break

print(answer)
