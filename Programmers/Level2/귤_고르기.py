# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    answer = 0
    cnt = k
    var = {}

    for t in tangerine:
        var[t] = var.get(t, 0) + 1
    sorted_items = sorted(var.items(), key=lambda x:x[1], reverse = True)

    for key, value in sorted_items:
        if cnt <= 0:
            break
        cnt -= value
        answer += 1

    return answer
