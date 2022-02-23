# https://www.acmicpc.net/problem/10828\

import sys

Stack = []
N = int(sys.stdin.readline())

for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        Stack.append(order[1])
    elif order[0] == "pop":
        if len(Stack) > 0:
            print(Stack[-1])
            del Stack[-1]
        else:
            print("-1")
    elif order[0] == "size": 
        print(len(Stack))
    elif order[0] == "empty":
        if len(Stack) > 0:
            print("0")
        else:
            print("1")
    elif order[0] == "top":
        if len(Stack) > 0:
            print(Stack[-1])
        else:
            print("-1")