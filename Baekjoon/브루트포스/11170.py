# https://www.acmicpc.net/problem/11170

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    cnt = 0
    for i in range(n, m + 1):
        cnt += str(i).count('0')
    print(cnt)