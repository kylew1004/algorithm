# https://www.acmicpc.net/problem/1406

import sys
input = sys.stdin.readline

stack = list(input().rstrip())
cursor = []
n = int(input())

for i in range(n):
    cmd = input().split()
    if cmd[0] == 'L' and stack:
        cursor.append(stack.pop())
    elif cmd[0] == 'D' and cursor:
        stack.append(cursor.pop())
    elif cmd[0] == 'B' and stack:
        stack.pop()
    elif cmd[0] == 'P':
        stack.append(cmd[1])
        
print(''.join(stack + cursor[::-1]))
