# https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)

    for i in range(len(score)):
        if (i + 1) % m == 0:
            answer += score[i] * m
    return answer