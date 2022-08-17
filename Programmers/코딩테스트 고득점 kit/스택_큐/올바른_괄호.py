# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = False
    cnt = 0

    for ss in list(s):
        if ss == '(':
            cnt += 1
        elif ss == ')':
            if cnt <= 0:
                return False
            cnt -= 1

    if not cnt:
        answer = True

    return answer