# https://www.acmicpc.net/problem/4999

import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

if len(a) >= len(b):
    print('go')
else:
    print('no')