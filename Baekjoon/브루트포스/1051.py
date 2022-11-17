# https://www.acmicpc.net/problem/1051

n, m = map(int,input().split())
answer = []
square = [list(input()) for _ in range(n)]
min_num = min(n, m)

for i in range(n):
    for j in range(m):
        for k in range(min_num):
            if (i + k) < n and (j + k) < m and square[i][j] == square[i][j + k] == square[i + k][j] == square[i + k][j + k]:
                answer.append((k + 1) ** 2)

print(max(answer))
