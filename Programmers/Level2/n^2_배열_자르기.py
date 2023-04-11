# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        a, b = divmod(i, n)
        answer.append(max(a, b) + 1)

    return answer