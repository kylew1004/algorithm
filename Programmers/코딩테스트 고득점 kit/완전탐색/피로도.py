# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations
    
def solution(k, dungeons):
    answer = -1
    array = list(permutations(dungeons, len(dungeons)))

    for arr in array:
        nk = k
        result = 0
        for a in arr:
            if a[0] > nk:
                break
            else:
                nk -= a[1]
                result += 1
        if nk >= 0:
            answer = max(answer, result)
    
    return answer