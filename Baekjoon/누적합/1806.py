# https://www.acmicpc.net/problem/1806

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
total = 0
min_length = 100001

while True:
    if total >= s:
        total -= arr[start]
        start += 1
        min_length = min(min_length, end - start + 1)
    elif end == n:
        break
    else:
        total += arr[end]
        end += 1

if min_length == 100001:
    print(0)
else:
    print(min_length)
