# https://school.programmers.co.kr/learn/courses/30/lessons/250136#

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(land):
    answer = 0
    depth = len(land)
    length = len(land[0])
    visited = [[False] * length for _ in range(depth)]
    land_info = [[0] * length for _ in range(depth)]
    oil_info = {}
    
    queue = deque()
    oil_idx = 0
    
    for a in range(depth):
        for b in range(length):
            if visited[a][b] or land[a][b] == 0:
                continue
            cnt = 0
            queue.append([a, b])
            oil_idx += 1

            while queue:
                x, y = queue.popleft()
                
                if land[x][y] == 1 and not visited[x][y]:
                    land_info[x][y] = oil_idx
                    cnt += 1
                    visited[x][y] = True

                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx < 0 or nx >= depth or ny < 0 or ny >= length:
                            continue
                        queue.append([nx, ny])
            
            oil_info[oil_idx] = cnt

    for y in range(length):
        get_oil = 0
        visited_oil = [False] * (len(oil_info) + 1)
        
        for x in range(depth):
            if land[x][y] == 0:
                continue
            if visited_oil[land_info[x][y]]:
                continue
            if land_info[x][y] == 0:
                continue
            oil_num = land_info[x][y]
            
            get_oil += oil_info[oil_num]
            visited_oil[oil_num] = True

        answer = max(answer, get_oil)

    return answer