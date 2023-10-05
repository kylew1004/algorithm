# https://www.acmicpc.net/problem/2857

import sys
input = sys.stdin.readline

names = [input().rstrip() for _ in range(5)]
ans = []

for i in range(5):
    if 'FBI' in names[i]:
        ans.append(i + 1)

if ans:
    print(*ans)
else:
    print('HE GOT AWAY!')
