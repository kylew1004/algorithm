# https://www.acmicpc.net/problem/10569

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    v, e = map(int, input().split())
    print(2 - v + e)