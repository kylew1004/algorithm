# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ""
    alpha = [chr(i) for i in range(97, 123)]
    
    for ch in skip:
        if ch in alpha:
            alpha.remove(ch)
    
    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)]
        answer += change

    return answer