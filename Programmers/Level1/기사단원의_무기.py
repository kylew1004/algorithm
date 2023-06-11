# https://school.programmers.co.kr/learn/courses/30/lessons/136798

from math import sqrt

def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(sqrt(i)) + 1):
            if i % j == 0 :
                if j == i // j:
                    cnt += 1
                else :
                    cnt += 2
            if cnt > limit :
                cnt = power
                break
        answer += cnt

    return answer