# https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = []
    for _ in range(n):
        apply, interview = map(int, input().split())
        data.append((apply, interview))

    data.sort(key = lambda x: x[1])
    min = data[0][0]
    count = 1
    
    for i in range(1, n):
        if data[i][0] < min:
            min = data[i][0]
            count += 1

    print(count)