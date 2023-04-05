# https://www.acmicpc.net/problem/1197

v, e = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(e)]
arr.sort(key = lambda x : x[2])
parent = list(range(v + 1))
sum = 0


def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])

    return parent[a]


for a, b, c in arr:
    if find(a) != find(b):
        union(a, b)
        sum += c

print(sum)