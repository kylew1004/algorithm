# https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution(arr):
    arr.sort()
    biggest = arr[-1]
    answer = biggest
    
    while True:
        for i in range(len(arr) - 1):
            if answer % arr[i] != 0:
                break
        else: # for문이 끝까지 실행되었을 때
            return answer
        answer += biggest
