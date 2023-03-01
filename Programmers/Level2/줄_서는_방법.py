# https://school.programmers.co.kr/learn/courses/30/lessons/12936

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def solution(n, k):
    answer = []
    case = list(range(1, n + 1))

    while n != 0:
        boundary = factorial(n - 1)
        index = (k - 1) // boundary
        k = k % boundary
        answer.append(case.pop(index))
        n -= 1

    return answer
