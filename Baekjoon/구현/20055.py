# https://www.acmicpc.net/problem/20055

from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)

answer = 0

while belt.count(0) < k:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    if sum(robot):
        for i in range(n-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and belt[i +1] >= 1:
                robot[i + 1] = 1
                robot[i] = 0
                belt[i + 1] -= 1
        robot[-1] = 0
    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    answer += 1

print(answer)
