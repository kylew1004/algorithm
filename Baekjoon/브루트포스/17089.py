# https://www.acmicpc.net/problem/17089

n, m = map(int, input().split())
relations = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int , input().split())
    relations[a].append(b)
    relations[b].append(a)
answer = float('inf')

for i in range(1, n + 1):
    for j in relations[i]:
        for k in relations[j]:
            if k in relations[i]:
                answer = min(answer, len(relations[i]) + len(relations[j]) + len(relations[k]) - 6)

print(answer if answer != float('inf') else -1)
