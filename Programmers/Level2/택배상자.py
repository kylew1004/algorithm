# https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution(order):
    arr = []
    i = 1
    answer = 0

    while i != len(order) + 1:
        arr.append(i)
        while arr and arr[-1] == order[answer]:
            answer += 1
            arr.pop()
            
        i += 1
    return answer