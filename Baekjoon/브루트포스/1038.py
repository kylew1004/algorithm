# https://www.acmicpc.net/problem/1038

from itertools import combinations

n = int(input())
num = []

for i in range(1, 11):
    for comb in combinations(range(10), i):
        comb = sorted(list(comb), reverse = True)
        num.append(int("".join(map(str, comb))))
num.sort()

print(num[n] if len(num) > n else -1)
