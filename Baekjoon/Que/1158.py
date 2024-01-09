# https://www.acmicpc.net/problem/1158

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque([i for i in range(1, n + 1)])
ans = []

while queue:
    queue.rotate(-k + 1)
    ans.append(queue.popleft())
    
print('<' + ', '.join(map(str, ans)) + '>')