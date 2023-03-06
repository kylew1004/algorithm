# https://school.programmers.co.kr/learn/courses/30/lessons/17677

import math

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    str1_dic, str2_dic = {}, {}
    both, total = 0, 0
    
    word = ''
    for s in str1:
        if s >= 'a' and s <= 'z':
            word += s
        else:
            word = ''
            continue
        if len(word) == 2:
            str1_dic[word] = str1_dic.get(word, 0) + 1
            word = word[1]
    word = ''
    for s in str2:
        if s >= 'a' and s <= 'z':
            word += s
        else:
            word = ''
            continue
        if len(word) == 2:
            str2_dic[word] = str2_dic.get(word, 0) + 1
            word = word[1]

    for s in str1_dic:
        if str2_dic.get(s, 0):
            both += min(str1_dic[s], str2_dic[s])
            total += max(str1_dic[s], str2_dic[s])
        else:
            total += str1_dic[s]
    for s in str2_dic:
        if not str1_dic.get(s, 0):
            total += str2_dic[s]
    if total == 0:
        answer = 65536
    else:
        answer = math.floor(both / total * 65536)

    return answer
