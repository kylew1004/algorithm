# https://www.acmicpc.net/problem/1075

import sys
input = sys.stdin.readline

n = int(input())
f = int(input())
n -= n % 100

while n % f != 0:
    n += 1

print(str(n)[-2:])
