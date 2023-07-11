# https://www.acmicpc.net/problem/11931

import sys, heapq
input = sys.stdin.readline

# heap으로 정렬하는 방법

n = int(input())
arr = []

for _ in range(n):
    heapq.heappush(arr, -int(input()))

for _ in range(n):
    print(-heapq.heappop(arr))


'''
# sort로 정렬하는 방법

arr.sort(reverse=True)

for i in arr:
    print(i)
'''