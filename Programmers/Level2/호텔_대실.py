# https://school.programmers.co.kr/learn/courses/30/lessons/155651

import heapq

def solution(book_time):
    answer = 1
    
    times = [[int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])] for s, e in book_time]
    times.sort()
    heap = []
    
    for start, end in times:
        if not heap:
            heapq.heappush(heap, end)
            continue
        if heap[0] <= start:
            heapq.heappop(heap)
        else:
            answer += 1
        heapq.heappush(heap, end + 10)
    
    return answer