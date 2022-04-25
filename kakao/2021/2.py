# https://tech.kakao.com/2021/07/08/2021-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-for-tech-developers-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%95%B4%EC%84%A4/

import sys
input = sys.stdin.readline

places = []
for i in range(5):
    places.append(list(map(str, input().split())))
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
crosses = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
res = []

def solution(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] != "P":
                continue
            
            for dx, dy in moves:
                x, y = i + dx, j + dy
                if 0 <= x < 5 and 0 <= y < 5 and place[x][y] == "P":
                    return 0
                        
            for dx, dy in crosses:
                x, y = i + dx, j + dy
                if 0 <= x < 5 and 0 <= y < 5 and place[x][y] == "P":
                    if place[i][y] != "X" or place[x][j] != "X":
                        return 0
                    
            for dx, dy in moves:
                x, y = i + 2 * dx, j + 2 * dy
                if 0 <= x < 5 and 0 <= y < 5 and place[x][y] == "P":
                    if place[i + dx][j + dy] != "X":
                        return 0
    return 1

for place in places:
    res.append(solution(place))
print(res)