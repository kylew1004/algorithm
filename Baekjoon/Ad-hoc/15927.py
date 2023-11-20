# https://www.acmicpc.net/problem/15927

import sys, math
input = sys.stdin.readline

s = input().rstrip()

if s == s[0] * len(s):
    print(-1)
elif s != s[::-1]:
    print(len(s))
else:
    print(len(s) - 1)