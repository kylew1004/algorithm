# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = 0
    cnt = bin(n).count("1")

    for i in range(n + 1, 1000001):
        if cnt == bin(i).count("1"):
            answer = i
            break

    return answer
