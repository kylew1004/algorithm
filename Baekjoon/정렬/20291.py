# https://www.acmicpc.net/problem/20291

import sys
input = sys.stdin.readline

n = int(input())
ext = {}

for _ in range(n):
    name, extention = input().rstrip().split('.')
    if extention in ext:
        ext[extention] += 1
    else:
        ext[extention] = 1
        
for key, value in sorted(ext.items()):
    print(key, value)