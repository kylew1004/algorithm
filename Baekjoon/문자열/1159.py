# https://www.acmicpc.net/problem/1159

import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for _ in range(n):
    s = input().rstrip()
    dic[s[0]] = dic.get(s[0], 0) + 1

res = [k for k, v in dic.items() if v >= 5]

print(''.join(sorted(res)) if res else 'PREDAJA')