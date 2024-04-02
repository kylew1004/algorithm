# https://www.acmicpc.net/problem/9063

import sys
input = sys.stdin.readline

n = int(input())
x, y = [], []

for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

width = max(x) - min(x)
height = max(y) - min(y)

print(width * height)
