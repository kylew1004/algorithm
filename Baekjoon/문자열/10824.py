# https://www.acmicpc.net/problem/10824

import sys
input = sys.stdin.readline

a, b, c, d = input().split()
a = int(a + b)
c = int(c + d)
print(a + c)
