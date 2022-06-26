# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    result = {}
    total = len(stages)
    for stage in range(1, N+1):
        if total != 0:
            count = stages.count(stage)
            result[stage] = count / total
            total -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)