# https://school.programmers.co.kr/learn/courses/30/lessons/172927

import math

def solution(picks, minerals):
    answer = 0
    cnt = [[0, 0, 0, 0] for _ in range(math.ceil(len(minerals) / 5))] # [dia, iron, stone, total]
    minerals_length = len(minerals)

    for i in range(minerals_length):
        idx = i // 5
        if minerals[i] == "diamond":
            cnt[idx][0] += 1
        elif minerals[i] == "iron":
            cnt[idx][1] += 1
        elif minerals[i] == "stone":
            cnt[idx][2] += 1
        if (i + 1) % 5 == 0 or (i + 1) == minerals_length:
            cnt[idx][3] = 25 * cnt[idx][0] + 5 * cnt[idx][1] + cnt[idx][2]
    
    if minerals_length > 5 * sum(picks):
        cnt.pop()

    cnt.sort(key=lambda x : x[3], reverse=True)

    for i in range(len(cnt)):
        if picks[0]:
            answer += sum(cnt[i][0:3])
            picks[0] -= 1
        elif picks[1]:
            answer += 5 * cnt[i][0] + sum(cnt[i][1:3])
            picks[1] -= 1
        elif picks[2]:
            answer += cnt[i][3]
            picks[2] -= 1

    return answer