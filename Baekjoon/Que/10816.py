# https://www.acmicpc.net/problem/10816

#이진탐색으로 풀려니까 계속 시간초과가 발생했다. 힙과 딕셔너리로 해결했는데 이게 왜 이진탐색으로 분류된건지 모르겠다.

import sys, heapq
input = sys.stdin.readline

n = int(input())
hold = sorted(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))
count = {}

while hold:
    num = heapq.heappop(hold)
    count[num] = count.get(num, 0) + 1

for num in nums:
    print(count.get(num, 0), end = ' ')