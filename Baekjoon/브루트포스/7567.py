# https://www.acmicpc.net/problem/7567

import sys
input = sys.stdin.readline

s = input().strip()
result = 10

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        result += 5
    else:
        result += 10

print(result)