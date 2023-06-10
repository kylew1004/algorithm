# https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0
    
    while n >= a:
        tmp = (n // a) * b
        answer += tmp
        n = tmp + (n % a)

    return answer