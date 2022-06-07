# https://programmers.co.kr/learn/courses/30/lessons/42842

def divisor(num):
    y = []
    i = 1
    while i*i <= num:
        if num % i == 0:
            y.append(i)
        i += 1
    return y

def solution(brown, yellow):
    answer = []
    yy = divisor(yellow)
    
    for y in yy:
        w = (yellow//y)+2
        h = y+2
        if w*h == brown+yellow:
            answer = [w,h]
            return answer
    return answer