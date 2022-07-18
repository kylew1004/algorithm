# https://www.acmicpc.net/problem/16637

import sys

length = int(input())
line = list(input())
answer = -(sys.maxsize)

def calculate(num1, op, num2):
    if op == '*':
        return num1 * num2
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2

def dfs(idx, num):
    global answer

    if idx == length - 1:
        answer = max(answer, num)
        return

    if idx + 2 < length:
        dfs(idx + 2, calculate(num, line[idx + 1], int(line[idx + 2])))

    if idx + 4 < length:
        dfs(idx + 4, calculate(num, line[idx + 1], calculate(int(line[idx + 2]), line[idx + 3], int(line[idx + 4]))))


dfs(0, int(line[0]))
print(answer)