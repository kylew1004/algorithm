# https://school.programmers.co.kr/learn/courses/30/lessons/17681

# 풀이 참조를 했다. zfill 함수라는 걸 처음알았는데 문자열 길이를 정하고 남는 부분은 0으로 채워주는 함수다.
# rjust, ljust 라는 함수도 비슷한데 각각 오른쪽 왼쪽 정렬을 해주는 기능을 가지고 있다. 다만 이 함수들은 0대신 다른 문자를 채울 수 있다.

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        answer.append(bin(arr1[i] | arr2[i])[2:].zfill(n))
        answer[i] = answer[i].replace('0', ' ')
        answer[i] = answer[i].replace('1', '#')
        
    return answer
