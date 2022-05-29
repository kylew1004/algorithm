# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        num1 = heapq.heappop(scoville)
        num2 = heapq.heappop(scoville)
        heapq.heappush(scoville, num1 + num2 * 2)
        count += 1
    return count if scoville[0] >= K else -1