# https://www.acmicpc.net/problem/4949

import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':
        break
    stack = []
    flag = True
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break
    if flag and not stack:
        print('yes')
    else:
        print('no')
