# https://www.acmicpc.net/problem/2675

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    for i in s:
        print(i * r, end='')
    print()
