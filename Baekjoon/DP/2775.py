# https://www.acmicpc.net/problem/2775

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    floor = int(input())
    room = int(input())
    
    people = [[0] * room for _ in range(floor + 1)]
    
    for i in range(room):
        people[0][i] = i + 1
    
    for i in range(1, floor + 1):
        for j in range(room):
            people[i][j] += sum(people[i - 1][:j + 1])
    
    print(people[floor][room - 1])