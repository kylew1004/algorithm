# https://www.acmicpc.net/problem/1120

import sys
input = sys.stdin.readline

a, b = input().split()
array = list()

for i in range(len(b) - len(a) + 1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[j + i]:
            cnt += 1
    array.append(cnt)

print(min(array))
