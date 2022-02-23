# https://www.acmicpc.net/problem/10845
import sys

Que = []
N = int(sys.stdin.readline())

for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        Que.append(order[1])
    elif order[0] == "pop":
        if len(Que) > 0:
            print(Que[0])
            del Que[0]
        else:
            print("-1")
    elif order[0] == "size": 
        print(len(Que))
    elif order[0] == "empty":
        if len(Que) > 0:
            print("0")
        else:
            print("1")
    elif order[0] == "front":
        if len(Que) > 0:
            print(Que[0])
        else:
            print("-1")
    elif order[0] == "back":
        if len(Que) > 0:
            print(Que[-1])
        else:
            print("-1")