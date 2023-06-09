# https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = date[(sum(month[:a - 1]) + b - 1) % 7] 
    return answer