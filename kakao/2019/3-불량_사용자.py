# https://school.programmers.co.kr/learn/courses/30/lessons/64064

from itertools import permutations

def isSame(banned_id, case):
    for i in range(len(case)):
        if len(case[i]) != len(banned_id[i]):
            return False
        for j in range(len(case[i])):
            if banned_id[i][j] != "*" and case[i][j] != banned_id[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    
    cases = permutations(user_id, len(banned_id))
    for case in cases:
        if isSame(banned_id, case):
            case = set(case)        # set를 시켜서 리스트에 추가하면 permutation 순서도 사라진다. product처럼 되서 유용!
            if case not in answer:
                answer.append(case)

    return len(answer)