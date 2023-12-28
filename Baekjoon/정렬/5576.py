# https://www.acmicpc.net/problem/5576

import sys
input = sys.stdin.readline

w = [int(input()) for _ in range(10)]
k = [int(input()) for _ in range(10)]

w.sort(reverse=True)
k.sort(reverse=True)

print(sum(w[:3]), sum(k[:3]))