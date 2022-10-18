# https://www.acmicpc.net/problem/16943

from itertools import permutations

a, b = input().split()
b = int(b)
num = list(map(''.join, list(permutations(a))))
answer = -1

for n in num:
    first = n[0]
    n = int(n)
    if b >= n and first != '0':
        answer = max(answer, n)

print(answer)
