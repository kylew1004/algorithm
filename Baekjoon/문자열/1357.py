# https://www.acmicpc.net/problem/1357

import sys
input = sys.stdin.readline

def reverse(x):
    return int(str(x)[::-1])

x, y = map(int, input().split())
print(reverse(reverse(x) + reverse(y)))