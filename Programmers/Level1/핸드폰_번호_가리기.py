# https://school.programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = ''
    length = len(phone_number)
    answer = '*' * (length - 4) + phone_number[-4:]

    return answer
