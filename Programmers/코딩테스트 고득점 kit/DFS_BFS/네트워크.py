# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

def solution(n, computers):

    def bfs(idx):
        queue = deque()
        queue.append(idx)

        while queue:
            q = queue.popleft()
            visited[q] = 1
            for i in range(n):
                if computers[q][i] and not visited[i]:
                     queue.append(i)

    answer = 0
    visited = [0 for i in range(n)]
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1

    return answer