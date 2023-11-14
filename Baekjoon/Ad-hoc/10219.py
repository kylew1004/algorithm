# https://www.acmicpc.net/problem/10219

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    for _ in range(h):
        print(input().rstrip()[::-1])