# https://www.acmicpc.net/problem/1543

import sys
input = sys.stdin.readline

data = input().rstrip()
target = input().rstrip()
start = 0
count = 0

while start <= len(data) - len(target):
    if data[start : start + len(target)] == target:
        count += 1
        start += len(target)
    else:
        start += 1

print(count)
