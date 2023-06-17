# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    info = {n : y for n, y in zip(name, yearning)}
    
    for targets in photo:
        score = 0
        for key in targets:
            if key in info.keys():
                score += info[key]
        answer.append(score)
    
    return answer