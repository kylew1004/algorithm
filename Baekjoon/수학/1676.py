# https://www.acmicpc.net/problem/1676

import sys
input = sys.stdin.readline

n = int(input())
print(n // 5 + n // 25 + n // 125)