# https://www.acmicpc.net/problem/1092

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
crane.sort(reverse = True)
box.sort(reverse = True)

if box[0] > crane[0]:
    print(-1)
else:
    answer = 0
    while box:
        for i in range(n):
            for j in range(len(box)):
                if crane[i] >= box[j]:
                    del box[j]
                    break
        answer += 1

    print(answer)
