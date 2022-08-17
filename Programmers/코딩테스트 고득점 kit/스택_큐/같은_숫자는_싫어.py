# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    tmp = ''
    for a in arr:
        if tmp != a:
            tmp = a
            answer.append(a)
    return answer