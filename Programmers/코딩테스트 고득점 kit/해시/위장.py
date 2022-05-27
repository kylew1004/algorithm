# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    cloth = {}
    answer = 1
    for i, j in clothes:
        if j not in cloth:
            cloth[j] = 1
        else:
            cloth[j] += 1

    for x in cloth.values():
        answer = answer * (x + 1)
    answer -= 1
    return answer
