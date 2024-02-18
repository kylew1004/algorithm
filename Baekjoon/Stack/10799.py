# https://www.acmicpc.net/problem/10799

import sys
input = sys.stdin.readline

s = input().strip()
stack = []
answer = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else:
        stack.pop()
        if s[i - 1] == "(":
            answer += len(stack)
        else:
            answer += 1

print(answer)