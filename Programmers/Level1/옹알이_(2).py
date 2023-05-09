# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    answer = 0

    for bab in babbling:
        for word in ['aya','ye','woo','ma']:
            if word * 2 not in bab:
                bab = bab.replace(word, " ")

        if bab.split() == []:
            answer += 1

    return answer