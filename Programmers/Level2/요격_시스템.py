# https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    answer = 0
    targets.sort(key=lambda x:(x[1], x[0]))
    s, e = 0, 0
    
    for x, y in targets:
        if e <= x:
            answer += 1
            e = y
            
    return answer
