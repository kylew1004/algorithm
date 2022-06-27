# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    length = len(citations)

    for i in range(1, length + 1):
        cnt1 = 0
        cnt2 = 0
        for j in range(length):
            if citations[j] >= i:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 >= i and cnt2 <= i and i > answer:
            answer = i

    return answer