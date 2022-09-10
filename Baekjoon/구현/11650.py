# https://www.acmicpc.net/problem/11650

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

matrix.sort()

for i in range(n):
    print(matrix[i][0], matrix[i][1])