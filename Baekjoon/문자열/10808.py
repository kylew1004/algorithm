# https://www.acmicpc.net/problem/10808

import sys
input = sys.stdin.readline

s = input().rstrip()
arr = [0] * 26

for i in s:
    arr[ord(i) - 97] += 1

print(*arr)
