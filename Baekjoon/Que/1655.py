# https://www.acmicpc.net/problem/1655

import heapq
import sys

input = sys.stdin.readline

n = int(input())
left, right = [], [] 

for i in range(n):
  num = int(input())

  if len(left) == len(right):
    heapq.heappush(left, (-num, num))
  else:
    heapq.heappush(right, (num, num))

  if i > 0 and left[0][1] > right[0][1]:
    nl = heapq.heappop(left)[1]
    nr = heapq.heappop(right)[1]
    heapq.heappush(left, (-nr, nr))
    heapq.heappush(right, (nl, nl))

  print(left[0][1])
