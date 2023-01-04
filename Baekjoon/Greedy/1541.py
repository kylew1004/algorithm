# https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline

arr = input().split('-')
s = 0

for num in arr[0].split('+'):
    s += int(num)

for num in arr[1:]:
    for n in num.split('+'):
        s -= int(n)

print(s)
