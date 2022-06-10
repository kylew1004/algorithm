# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    number =list(number)
    result=[number.pop(0)]
    for n in number:
        while result and result[-1] < n and k>0:
            result.pop()
            k -= 1
        result.append(n)
            
    if k :
        result=result[:-k]
    answer = ''.join(result)

    return answer