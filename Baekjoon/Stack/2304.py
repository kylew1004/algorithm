# https://www.acmicpc.net/problem/2304

import sys
input = sys.stdin.readline

n = int(input())
buildings = [0] * 1001
max_height = 0
max_idx = 0

for _ in range(n):
    l, h = map(int, input().split())
    buildings[l] = h
    if h > max_height:
        max_height = h
        max_idx = l
        
left = 0
right = 0
area = 0

for i in range(max_idx + 1):
    if buildings[i] > left:
        left = buildings[i]
    area += left
    
for i in range(1000, max_idx, -1):
    if buildings[i] > right:
        right = buildings[i]
    area += right
    
print(area)