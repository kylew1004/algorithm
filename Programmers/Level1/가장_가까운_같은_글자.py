# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    
    dic = {}
    cnt = 0
    for i in list(s):
        dic[i] = dic.get(i, [])
        if not dic[i]:
            answer.append(-1)
        else:
            answer.append(cnt - dic[i][-1])
        dic[i].append(cnt)
        cnt += 1

    return answer
