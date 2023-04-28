# https://www.acmicpc.net/problem/2110

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
nodes = [int(input()) for _ in range(n)]
nodes.sort()

start, end = 1, nodes[-1] - nodes[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    node = nodes[0]

    for i in range(1, n):
        if nodes[i] - node >= mid:
            cnt += 1
            node = nodes[i]

    if cnt >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)