# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    stu = [0] * (n+2)

    for l in lost:
        stu[l] -= 1
    for r in reserve:
        stu[r] += 1

    for s in range(1, n+1):
        if stu[s] > 0:
            if stu[s-1] < 0:
                stu[s] -= 1
                stu[s-1] += 1
            elif stu[s+1] < 0:
                stu[s] -= 1
                stu[s+1] += 1

    for i in range(1, n+1):
        if stu[i] >= 0:
            answer += 1
    return answer