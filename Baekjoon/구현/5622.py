# https://www.acmicpc.net/problem/5622

import sys
input = sys.stdin.readline

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = input().rstrip()
ans = 0

for c in s:
    for i in range(len(dial)):
        if c in dial[i]:
            ans += i + 3
            break
        
print(ans)