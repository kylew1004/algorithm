# https://school.programmers.co.kr/learn/courses/30/lessons/181187
# 풀이 참고함

import math

def solution(r1, r2):
    answer = 0  
    
    for i in range(1, r2 + 1):
        height1 = math.sqrt(r2 ** 2 - i ** 2)
        height2 = 0 if i > r1 else math.sqrt(r1 ** 2 - i ** 2)

        answer += math.floor(height1) - math.ceil(height2) + 1

    return answer * 4