# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque

def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and not visited[i][j]:
                cnt = int(maps[i][j])
                visited[i][j] = True
                queue = deque()
                queue.append([i, j])
                while queue:
                    x, y = queue.popleft()
                    
                    for idx in range(4):
                        nx = x + dx[idx]
                        ny = y + dy[idx]
                        if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                            continue
                        if visited[nx][ny] or maps[nx][ny] == "X":
                            continue
                        cnt += int(maps[nx][ny])
                        visited[nx][ny] = True
                        queue.append([nx, ny])
                answer.append(cnt)
    
    if answer:
        answer.sort()
    else:
        answer.append(-1)
    
    return answer