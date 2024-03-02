# https://school.programmers.co.kr/learn/courses/30/lessons/142085

import heapq

def solution(n, k, enemy):
    answer = 0
    keep = []
    total = 0
    cnt = 0
    
    for i in range(len(enemy)):
        heapq.heappush(keep, -enemy[i])
        total += enemy[i]
        if total > n:
            while keep and cnt < k and total > n:
                total -= (-1) * heapq.heappop(keep)
                cnt += 1
        if cnt == k and total > n:
            break
        else:
            answer += 1
        
    return answer