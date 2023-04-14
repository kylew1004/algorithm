# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    codes = {chr(i + 64) : [i, 1] for i in range(1, 27)}    #번호, 길이
    length = len(msg)
    got_word = 0
    last = 27

    for i in range(length):
        if i < got_word:
            continue
        idx = msg[i]
        l = len(idx)
        got_word += 1
        answer.append(codes[idx][0])
        for j in range(i + 1, length + 1):
            word = msg[i:j]
            if word in codes:
                if codes[word][1] > l:  # 사전에 더 긴 단어가 있으면
                    answer.pop()
                    l = codes[word][1]
                    answer.append(codes[word][0])
                    got_word += 1
            else:               # 사전에 단어가 없으면
                codes[word] = [last, len(word)]
                last += 1
                break
    
    return answer