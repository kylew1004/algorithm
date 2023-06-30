# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer=[]
    key_dict = {}

    for km in keymap:
        for i in range(len(km)):
            key = km[i]
            if key not in key_dict:
                key_dict[key] = (i + 1)
            else:
                key_dict[key] = min(key_dict[key], i + 1)

    for target in targets:
        total = 0
        for t in target:
            if t in key_dict:
                total += key_dict[t]
            else:
                total = -1
                break
        answer.append(total)

    return answer