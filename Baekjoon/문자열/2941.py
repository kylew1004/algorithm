# https://www.acmicpc.net/problem/2941

import sys
input = sys.stdin.readline

s = input().rstrip()
cnt = 0
i = 0

while i < len(s):
    if s[i] == 'c':
        if i + 1 < len(s) and (s[i + 1] == '=' or s[i + 1] == '-'):
            i += 1
    elif s[i] == 'd':
        if i + 1 < len(s) and s[i + 1] == '-':
            i += 1
        elif i + 2 < len(s) and s[i + 1] == 'z' and s[i + 2] == '=':
            i += 2
    elif s[i] == 'l' or s[i] == 'n':
        if i + 1 < len(s) and s[i + 1] == 'j':
            i += 1
    elif s[i] == 's' or s[i] == 'z':
        if i + 1 < len(s) and s[i + 1] == '=':
            i += 1
    cnt += 1
    i += 1

print(cnt)
