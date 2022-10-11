# https://www.acmicpc.net/problem/1967

# 첫 번째 노드에서 가장 먼 노드를 찾고 그 노드에서 다시 가장 먼 노드를 찾으면 노드의 반지름이 된다.
# 이거 몰라서 시간초과늪에서 허우적거림; 힙정렬 쓰고 별 짓 다했는데 그게 문제가 아니었다.
# 처음에 각 노드마다 한 번씩 dfs를 돌려서 가장 먼 거리를 찾았는데 시간초과가 났다. 테스트케이스도 하나밖에 없어서 분석하기가 쉽지 않았음.

import sys
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y, length = map(int, input().split())
    tree[x].append([y, length])
    tree[y].append([x, length])
answer = 0
distance = [-1] * (n + 1)
distance[1] = 0
farthest_node = n


def find_farthest_node(node, cnt):
    global distance
    
    for next_node, length in tree[node]:
        if distance[next_node] == -1:
            distance[next_node] = cnt + length
            find_farthest_node(next_node, distance[next_node])


find_farthest_node(1, 0)

farthest_node = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[farthest_node] = 0
find_farthest_node(farthest_node, 0)
    
print(max(distance))