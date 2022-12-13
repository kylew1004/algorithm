# https://www.acmicpc.net/problem/1822

a, b = map(int, input().split())
A, B = {}, {}

for n in map(int, input().split()):
    A[n] = 1
for n in map(int, input().split()):
    B[n] = 1

result = []

for i in A:
    if i not in B:
        result += [i]

print(len(result))
print(*sorted(result))
