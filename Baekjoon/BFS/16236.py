# https://www.acmicpc.net/problem/16236

from collections import deque

n = int(input())
graph = []
answer = 0  # 시간
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        if nums[j] != 0:
            if nums[j] == 9:
                nums[j] = 0
                start = (i, j)
    graph.append(nums)
graph[start[0]][start[1]] = 0

def next_fish(i, j, size):
    visited = [[False] * n for _ in range(n)]
    visited[i][j] = True
    flag = True
    queue = deque([[i, j, 0]])
    r, c, distance = float('inf'), float('inf'), float('inf')
    
    while queue:
        x, y, d = queue.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] <= size:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if graph[nx][ny] != 0 and graph[nx][ny] < size:
                        flag = False
                        if nx > r:
                            continue
                        elif nx == r and ny > c:
                            continue
                        if distance >= d + 1:
                            r, c, distance = nx, ny, d + 1
                    if flag:
                        queue.append([nx, ny, d + 1])

    return [(r, c), distance]


queue = deque([start])
size = 2
eaten = 0

while queue:
    x, y = queue.popleft()
    if eaten == size:
        size += 1
        eaten = 0
    (nx, ny), distance = next_fish(x, y, size)
    if distance == float('inf'):
        break
    queue.append((nx, ny))
    answer += distance
    eaten += 1
    graph[nx][ny] = 0

print(answer)
