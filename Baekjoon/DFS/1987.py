# https://www.acmicpc.net/problem/1987
# dfs로 풀면 pypy3으로만 가능함 , bfs랑 set로 풀면 python3으로도 가능함
# 문제 유형을 보면 bfs로 푸는게 유리해 보이는데 왜 dfs로 되있는지 모르겠다.

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(map(lambda x : ord(x) - 65, input())) for _ in range(r)]
alphabet = [False] * 26
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0


def dfs(x, y, cnt):
    global answer

    answer = max(answer, cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            target = arr[nx][ny]
            if not alphabet[arr[nx][ny]]:
                alphabet[target] = True
                dfs(nx, ny, cnt + 1)
                alphabet[target] = False

alphabet[arr[0][0]] = True
dfs(0, 0, 1)
print(answer)