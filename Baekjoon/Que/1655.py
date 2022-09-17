# https://www.acmicpc.net/problem/1655

import heapq
import sys

input = sys.stdin.readline

n = int(input())
left, right = [], [] 

for i in range(n):
  num = int(input())

  if len(left) == len(right):
    heapq.heappush(left, -num)
  else:
    heapq.heappush(right, num)

  if i > 0 and -left[0] > right[0]:
    nl = heapq.heappop(left)
    nr = heapq.heappop(right)
    heapq.heappush(left, -nr)
    heapq.heappush(right, -nl)

  print(left[0] * -1)
