# https://www.acmicpc.net/problem/2217

n = int(input())
k = []
answers = []

for _ in range(n):
    k.append(int(input()))
k.sort()

for x in k:
    answers.append(x * n)
    n -= 1

print(max(answers))
