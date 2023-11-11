# https://www.acmicpc.net/problem/4153

import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0: break
    if a > b: a, b = b, a
    if b > c: b, c = c, b
    if a > b: a, b = b, a
    print('right' if a ** 2 + b ** 2 == c ** 2 else 'wrong')