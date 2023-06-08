# https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    answer = ''
    dict_x = {i : 0 for i in range(10)}
    dict_y = {i : 0 for i in range(10)}
    
    for i in X:
        dict_x[int(i)] += 1
    for i in Y:
        dict_y[int(i)] += 1
    
    for i in range(9, -1, -1):
        if dict_x[i] == 0 and dict_y[i] == 0:
            continue
        answer += min(dict_x[i], dict_y[i]) * str(i)
    
    if not answer:
        return "-1"
    else:
        if answer[0] == '0':
            return '0'
        else:
            return answer

    # return str(int(answer)) if answer else "-1" => 이거 시간초과 나는데 이유를 모르겠음