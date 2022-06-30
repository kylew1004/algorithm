# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    last = len(prices)

    for i in range(last-1):
        cnt = 0
        for j in range(i+1, last):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
    answer.append(0)
    
    return answer