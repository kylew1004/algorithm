# https://www.acmicpc.net/problem/16198

def dfs(marbles, total):
    global answer

    if len(marbles) == 3:
        total += marbles[0] * marbles[-1]
        answer = max(answer, total)
        return

    for idx in range(1, len(marbles) - 1):
        dfs(marbles[:idx] + marbles[idx + 1:], total + marbles[idx - 1] * marbles[idx + 1])


n = int(input())
marbles = list(map(int, input().split()))
answer = 0

dfs(marbles, 0)
print(answer)
