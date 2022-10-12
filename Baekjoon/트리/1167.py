# https://www.acmicpc.net/problem/1167

# 1967 트리의 지름과 사실상 같은문제

v = int(input())
tree = [[] for _ in range(v + 1)]
for _ in range(v):
    info = list(map(int, input().split()))
    for i in range(1, len(info) // 2):
        tree[info[0]].append([info[2 * i - 1], info[2 * i]])


def find_farthest_node(node, cnt):
    for next, cost in tree[node]:
        if distance[next] == -1:
            distance[next] = cnt + cost
            find_farthest_node(next, distance[next])


distance = [-1] * (v + 1)
distance[1] = 0
find_farthest_node(1, 0)
start = distance.index(max(distance))
distance = [-1] * (v + 1)
distance[start] = 0
find_farthest_node(start, 0)

print(max(distance))