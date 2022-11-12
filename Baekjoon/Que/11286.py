# https://www.acmicpc.net/problem/11286

import sys, heapq
input = sys.stdin.readline

n = int(input())
abs_heap = []

for i in range(n):
	num = int(input())
	if num:
		heapq.heappush(abs_heap, (abs(num), num))
	else:
		if abs_heap:
			print(heapq.heappop(abs_heap)[1])
		else:
			print(0)
