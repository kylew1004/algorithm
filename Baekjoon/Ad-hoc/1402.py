# https://www.acmicpc.net/problem/16956

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
field = [list(input().rstrip()) for _ in range(r)]

for i in range(r):
    for j in range(c):
        if field[i][j] == 'W':
            if i > 0 and field[i - 1][j] == 'S':
                print(0)
                exit()
            if i < r - 1 and field[i + 1][j] == 'S':
                print(0)
                exit()
            if j > 0 and field[i][j - 1] == 'S':
                print(0)
                exit()
            if j < c - 1 and field[i][j + 1] == 'S':
                print(0)
                exit()
            if i > 0 and field[i - 1][j] == '.':
                field[i - 1][j] = 'D'
            if i < r - 1 and field[i + 1][j] == '.':
                field[i + 1][j] = 'D'
            if j > 0 and field[i][j - 1] == '.':
                field[i][j - 1] = 'D'
            if j < c - 1 and field[i][j + 1] == '.':
                field[i][j + 1] = 'D'
                
print(1)
for row in field:
    print(''.join(row))