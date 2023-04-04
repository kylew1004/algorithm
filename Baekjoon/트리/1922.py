# https://www.acmicpc.net/problem/1922

n = int(input())
m = int(input())
array = [list(map(int, input().split())) for _ in range(m)]
array.sort(key = lambda x : x[2])
check = [i for i in range(n + 1)]
cnt = 0


def find(x):
    if check[x] == x:
        return x
    check[x] = find(check[x])
    return check[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        check[x] = y
    else:
        check[y] = x


for i in array:
    if find(i[0]) != find(i[1]):
        union(i[0], i[1])
        cnt += i[2]

print(cnt)
