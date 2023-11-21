# https://school.programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    answer = 2
    left, right = a[0], a[-1]

    for i in range(1, len(a) - 1):
        if left > a[i]:
            answer += 1
            left = a[i]
        if right > a[-i - 1]:
            answer += 1
            right = a[-i - 1]
    if left == right:
        answer -= 1

    return answer