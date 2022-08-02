# https://www.acmicpc.net/problem/14888

def dfs(idx, result, op):
    global max_answer, min_answer

    if idx == n:
        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)
    else:
        if op[0]:
            op[0] -= 1
            dfs(idx + 1, result + num[idx], op)
            op[0] += 1
        if op[1]:
            op[1] -= 1
            dfs(idx + 1, result - num[idx], op)
            op[1] += 1
        if op[2]:
            op[2] -= 1
            dfs(idx + 1, result * num[idx], op)
            op[2] += 1
        if op[3]:
            op[3] -= 1
            dfs(idx + 1, int(result / num[idx]), op)
            op[3] += 1

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
min_answer = float('inf')
max_answer = -float('inf')
dfs(1, num[0], op)

print(max_answer)
print(min_answer)