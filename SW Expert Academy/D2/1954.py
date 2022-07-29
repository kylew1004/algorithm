# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

# 더 나은 풀이

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
T = int(input())
answer = []

for _ in range(T):
    n = int(input())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, -1
    idx = 0             # 우하좌상 움직임
    check = n*n         # 반복문 멈추기위한 변수
    cnt = 1
    
    while cnt <= check:
        nx = x + moves[idx][0]
        ny = y + moves[idx][1]

        if 0 <= nx < n and 0 <= ny < n and not graph[nx][ny]:
            graph[x][y] = cnt
            cnt += 1
            x, y = nx, ny
        else:
            idx = (idx+1) % 4
    answer.append(graph)

for tc in range(T):
    print(f"#{tc+1}")
    length = len(answer[tc])
    for i in range(length):
        print(*answer[tc][i])



"""
# 처음 풀이
answer = []
tc = int(input())
for _ in range(tc):
    n = int(input())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0
    check = n * n
    cnt = 1
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    idx = 0

    def change(idx):
        
        return idx
    if n == 1:
        answer.append([1])
    else:
        while check >= cnt:
            if not graph[x][y]:
                graph[x][y] = cnt
                cnt += 1
            if (moves[idx][0] and x == n - 1) or (moves[idx][1] and y == n - 1):
                idx = change(idx)
            elif (x == n - 1 and y == 0):
                idx = change(idx)

            if graph[x + moves[idx][0]][y + moves[idx][1]]:
                idx = change(idx)
            else:
                x += moves[idx][0]
                y += moves[idx][1]
        answer.append(graph)


for i in range(tc):
    print(f"#{i+1}")
    length = len(answer[i])
    if length == 1:
        print(1)
    else:
        for j in range(length):
            print(' '.join(map(str, answer[i][j])))
"""