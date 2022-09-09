# https://www.acmicpc.net/problem/1062

import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

words = [0] * n
ans = 0
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    for x in temp:
        words[i] |= (1 << (ord(x) - ord('a')))

if m < 5:
    print(0)
else:
    need = ['a','c','t','i','n']
    candidiate = list(set(chr(i) for i in range(ord('a'), ord('z') + 1)) - set(need))

    for i in list(combinations(candidiate, m - 5)):
        each = 0
        res = 0

        for j in need:
            each |= (1 << (ord(j) - ord('a')))
        for j in i:
            each |= (1 << (ord(j) - ord('a')))

        for j in words:
            if each & j == j:
                res += 1

        if ans < res:
            ans = res
    print(ans)