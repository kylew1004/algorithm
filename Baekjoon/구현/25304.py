# https://www.acmicpc.net/problem/25304

import sys
input = sys.stdin.readline

x = int(input())
n = int(input())
total = 0

for _ in range(n):
    a, b = map(int, input().split())
    total += a * b

if total == x:
    print('Yes')
else:
    print('No')