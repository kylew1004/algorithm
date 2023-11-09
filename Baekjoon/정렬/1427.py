# https://www.acmicpc.net/problem/1427

import sys
input = sys.stdin.readline

n = input().rstrip()
arr = []

for i in n:
    arr.append(int(i))

arr.sort(reverse=True)
print(''.join(map(str, arr)))