# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import Counter

def solution(topping):
    answer = 0

    count = Counter(topping)
    check = set()

    for top in topping:
        count[top] -= 1
        check.add(top)

        if count[top] == 0:
            count.pop(top)
        if len(count) == len(check):
            answer += 1

    return answer
