# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_dict = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}
    
    for d in data:
        value = d[ext_dict[ext]]
        if value <= val_ext:
            answer.append(d)

    answer.sort(key = lambda x : x[ext_dict[sort_by]])
    return answer