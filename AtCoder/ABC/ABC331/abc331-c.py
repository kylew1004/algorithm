# https://atcoder.jp/contests/abc331/tasks/abc331_c

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
d = defaultdict(list)
answer = [0] * n

for i, a in enumerate(A):
    d[a].append(i)

total = 0
for i, d_list in sorted(d.items(), reverse=True):
    for j in d[i]:
        answer[j] = total
    total += i * len(d_list)

print(*answer)