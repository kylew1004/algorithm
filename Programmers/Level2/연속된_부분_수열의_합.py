# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = []
    start, end = 0, -1
    total = 0
    
    for i in range(len(sequence)):
        total += sequence[i] 
        end += 1
        if total > k:
            while total > k and start < end:
                total -= sequence[start]
                start += 1
        if total == k:
            if not answer:
                answer = [start, end]
            elif end - start < answer[1] - answer[0]:
                answer = [start, end]

    return answer