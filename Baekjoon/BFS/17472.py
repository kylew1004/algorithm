# https://www.acmicpc.net/problem/17472

from collections import deque

def bfs(x, y, isl_num):
    q = deque()
    q.append([x, y])
    isl_num_map[x][y] = isl_num

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and isl_num_map[nx][ny] == -1:
                if graph[nx][ny]:
                    isl_num_map[nx][ny] = isl_num
                    q.append([nx, ny])

def dfs(x, y, dir, bridge_dis, start):
    nx = x + dx[dir]
    ny = y + dy[dir]

    if not 0 <= nx < n or not 0 <= ny < m:
        return
    if graph[nx][ny] == 1:
        end = isl_num_map[nx][ny]
        if start == end:
            return
        if bridge_dis == 1:
            return
        else:
            isl_min_dis[start][end] = min(bridge_dis, isl_min_dis[start][end])
            return
    bridge_dis += 1
    dfs(nx, ny, dir, bridge_dis, start)

def find_min(cnt, index, end):
    global answer

    if cnt == end:
        q = deque()
        c = [0 for _ in range(isl_num)]
        isl_cnt, bridge_length = 1, 0
        for i in range(isl_num):
            if not c[i]:
                q.append(i)
                c[i] = 1
                while q:
                    x = q.popleft()
                    for nx in i2i[x]:
                        if select[i2i_bridge[x][nx]] and not c[nx]:
                            c[nx] = 1
                            q.append(nx)
                            isl_cnt += 1
                            bridge_length += isl_min_dis[x][nx]

        if isl_cnt == isl_num:
            answer = min(answer, bridge_length)
        return

    for i in range(index, bridge_num):
        select[i] = 1
        find_min(cnt + 1, i + 1, end)
        select[i] = 0


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
isl_num_map = [[-1] * m for _ in range(n)]      # isl_num_map: 각 섬에 번호가 붙여진 배열

isl_num = 0         # isl_num: 각 섬에 붙일 번호이자 섬의 개수
for i in range(n):
    for j in range(m):
        if graph[i][j] and isl_num_map[i][j] == -1:
            bfs(i, j, isl_num)
            isl_num += 1

isl_min_dis = [[10] * isl_num for _ in range(isl_num)]      # isl_min_dis: 두 섬사이의 최소 다리 길이를 저장한 배열
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            for k in range(4):
                dfs(i, j, k, 0, isl_num_map[i][j])

i2i_bridge = [[-1] * isl_num for _ in range(isl_num)]       # i2i_bridge: 두 섬을 연결한 다리의 번호를 저장한 배열
i2i = [[] for _ in range(isl_num)]                          # i2i: 현재 위치에서 어느 섬으로 이동할 수 있는지 저장한 배열
bridge_num = 0                                              # bridge_num: 각 다리에 붙일 번호이자 다리의 개수
for i in range(isl_num - 1):
    for j in range(i + 1, isl_num):
        if isl_min_dis[i][j] < 10:
            i2i_bridge[i][j] = bridge_num
            i2i_bridge[j][i] = bridge_num
            i2i[i].append(j)
            i2i[j].append(i)
            bridge_num += 1

select = [0 for _ in range(bridge_num)]                     # select: dfs로 어느 다리를 선택했는지 저장하는 배열
if isl_num % 2 == 0:
    start = isl_num // 2                                    # start: 다리를 몇 개부터 선택할지 정하는 변수
else:
    start = (isl_num // 2) + 1
answer = float('inf')
for i in range(start, bridge_num + 1):
    find_min(0, 0, i)

if answer == float('inf'):
    print(-1)
else:
    print(answer)