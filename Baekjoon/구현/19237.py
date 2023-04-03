# https://www.acmicpc.net/problem/19237
# 그냥 존나 힘들다.... 중간에 변수 뭐 빠뜨렸는지 몰라서 헤맴 3시간 보다가 sharks_looking 초기화를 안시킨거였음.
# 빡구현 빡치네, graph도 만들어놓고 보니 쓸데도 없었음. 그냥 smell_graph만 써도 됐음.
# 청소년 상어 때처럼 한마리씩 움직이는게 아니라 전부다 동시에 움직이기 때문에 new_graph를 만들어서 위치를 초기화 시켜야 했다. 그래서 graph를 안씀
# 그냥 코드가 거지같다. 근데 다시 풀고 싶지는 않음.

from collections import deque

n, m, k = map(int, input().split())
graph = []
smell_graph = [[[0, 0] for _ in range(n)] for _ in range(n)] # (상어번호, 남은시간)
sharks = {i : [] for i in range(1, m + 1)} # 상어의 위치
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            sharks[graph[i][j]] = [i, j]
            smell_graph[i][j] = [graph[i][j], k]

looking = list(map(int, input().split()))
sharks_look = {i : looking[i - 1] for i in range(1, m + 1)} # 상어가 보고 있는 방향
sharks_direct = {i : [list(map(int, input().split())) for _ in range(4)] for i in range(1, m + 1)}  # 상어가 보고 있는 방향(상하좌우순)에 따른 우선순위
survived = [True] * (m + 1)

moves = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
answer = 0


def delete_smell():
    for i in range(n):
        for j in range(n):
            if smell_graph[i][j][1] != 0 and new_graph[i][j] == 0:
                smell_graph[i][j][1] -= 1
            if smell_graph[i][j][0] != 0 and smell_graph[i][j][1] == 0:
                smell_graph[i][j] = [0, 0]


queue = deque([[smell_graph, sharks, sharks_look, sharks_direct, survived, m]])


while queue:
    smell_graph, sharks, sharks_look, sharks_direct, survived, cnt = queue.popleft()
    new_graph = [[0] * n for _ in range(n)]

    for i in range(1, m + 1):
        if not survived[i]:
            continue
        flag = False
        for j in range(4):  # 우선순위
            dx, dy = moves[sharks_direct[i][sharks_look[i] - 1][j]]
            nx, ny = sharks[i][0] + dx, sharks[i][1] + dy
            if not (0 <= nx < n and 0 <= ny < n) or smell_graph[nx][ny][0] != 0:    # 범위를 벗어나거나 냄새가 있는 곳이면
                continue
            flag = True
            sharks_look[i] = sharks_direct[i][sharks_look[i] - 1][j]
            break
        if not flag:
            for j in range(4):
                dx, dy = moves[sharks_direct[i][sharks_look[i] - 1][j]]
                nx, ny = sharks[i][0] + dx, sharks[i][1] + dy
                if (0 <= nx < n and 0 <= ny < n) and smell_graph[nx][ny][0] == i:   # 범위를 벗어나지 않고 자신의 냄새가 있는 곳이면
                    flag = True
                    sharks_look[i] = sharks_direct[i][sharks_look[i] - 1][j]
                    break
        if flag:
            if new_graph[nx][ny] != 0:
                survived[i] = False
                cnt -= 1
                continue
            sharks[i] = [nx, ny]
            new_graph[nx][ny] = i

    for i in range(n):
        for j in range(n):
            if new_graph[i][j] != 0:
                smell_graph[i][j] = [new_graph[i][j], k]

    delete_smell()
    answer += 1
    queue.append([smell_graph, sharks, sharks_look, sharks_direct, survived, cnt])
    if cnt == 1 or answer > 1000:
        break


if answer > 1000:
    print(-1)
else:
    print(answer)