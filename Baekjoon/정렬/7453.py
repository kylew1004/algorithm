# https://www.acmicpc.net/problem/7453
# defaultdict을 사용하면 시간초과가 난다. 신기하네
# pypy3로 해결

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
answer = 0

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
ab = {}
for a in A:
    for b in B:
        tmp = a+b
        if tmp in ab:
            ab[tmp] += 1
        else:
            ab[tmp] = 1

for c in C:
    for d in D:
        tmp = -(c+d)
        if tmp in ab:
            answer += ab[tmp]

print(answer)