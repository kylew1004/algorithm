# https://www.acmicpc.net/problem/10817

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
print(sorted([a, b, c])[1])
