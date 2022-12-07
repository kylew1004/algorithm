# https://www.acmicpc.net/problem/2346

n = int(input())
balloons = list(map(int, input().split()))
target = 0
answer = []
idx = [x for x in range(1,n + 1)]
tmp = balloons.pop(target)
answer.append(idx.pop(target))

while balloons:
    if tmp < 0:
        target = (target + tmp) % len(balloons)
    else:
        target = (target + tmp - 1) % len(balloons)
    tmp = balloons.pop(target)
    answer.append(idx.pop(target))

for i in answer:
    print(i, end=' ')
