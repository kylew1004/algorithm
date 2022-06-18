# https://programmers.co.kr/learn/courses/30/lessons/42586

# math.ceil 은 내림, math.floor는 올림, math.round는 반올림

import math

def solution(progresses, speeds):
    answer = []
    left = []
    total = len(progresses)

    for i in range(total):
        left.append(math.ceil((100-progresses[i])/speeds[i]))

    num = 1
    last = left[0]
    if total >= 1:
        if total == 1:
            answer.append(num)
            return answer
        for i in range(1, total):
            if i == total - 1:
                if last < left[i]:
                    answer.append(num)
                    num = 1
                else:
                    num += 1
                answer.append(num)
            elif last < left[i]:
                answer.append(num)
                last = left[i]
                num = 1
            else:
                num += 1
    
    return answer