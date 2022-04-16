# https://www.acmicpc.net/problem/2864

import sys
input = sys.stdin.readline

a, b = list(input().split())

max = int(''.join(a.replace("5", "6"))) + int(''.join(b.replace("5", "6")))
min = int(''.join(a.replace("6", "5"))) + int(''.join(b.replace("6", "5")))

print(min, max)