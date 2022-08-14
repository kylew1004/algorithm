# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

def bfs(node, tree, visited, wire, cnt):
    queue = deque()
    queue.append([node, visited])
    visited[node] = True

    while queue:
        n, v = queue.popleft()
        cnt += 1

        for i in tree[n]:
            if not ((n == wire[0] and i == wire[1]) or (n == wire[1] and i == wire[0])):
                if not v[i]:
                    v[i] = True
                    queue.append([i, v])

    return cnt


def solution(n, wires):
    answer = float('inf')
    tree = [[] for _ in range(n + 1)]

    for wire in wires:
        a, b = wire
        tree[a].append(b)
        tree[b].append(a)

    for wire in wires:
        visited = [False] * (n + 1)
        temp = []
        for i in range(1, n + 1):
            if not visited[i]:
                cnt = bfs(i, tree, visited, wire, 0)
                temp.append(cnt)

        answer = min(answer, abs(temp[0] - temp[1]))

    return answer