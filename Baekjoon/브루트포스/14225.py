# https://www.acmicpc.net/problem/14225

n = int(input())
arr = list(map(int, input().split()))
answer = []

def dfs(value, index):
    if index == n:
        return 0;
    value += arr[index]
    answer.append(value)
    dfs(value, index+1)
    value -= arr[index]
    dfs(value, index+1)

dfs(0,0)
a = set(answer)
num = 0

while True:
    num += 1
    if num not in a:
        print(num)
        break