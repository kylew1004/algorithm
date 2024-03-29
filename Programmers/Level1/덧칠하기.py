# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    answer = 0
    painted = 0

    for s in section:
        if s >= painted:
            painted = s + m
            answer += 1

    return answer