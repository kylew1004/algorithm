# https://school.programmers.co.kr/learn/courses/30/lessons/140107

import math

def solution(k, d):
    answer = 0

    for i in range(0, d + 1, k):
        distance = math.floor(math.sqrt(d ** 2 - i ** 2))
        answer += (distance // k) + 1

    return answer