# https://www.acmicpc.net/problem/2745

import sys
input = sys.stdin.readline

n, b = input().split()
b = int(b)
ans = 0

for i in range(len(n)):
    if n[-i - 1].isdigit():
        ans += int(n[-i - 1]) * b ** i
    else:
        ans += (ord(n[-i - 1]) - 55) * b ** i

print(ans)
