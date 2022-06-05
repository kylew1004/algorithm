# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = [0, 0, 0]
    answer = []
    for i in range(len(answers)):
        if answers[i] == one[i % 5]:
            result[0] += 1
        if answers[i] == two[i % 8]:
            result[1] += 1
        if answers[i] == three[i % 10]:
            result[2] += 1
       
    a = max(result)
    
    for i in range(len(result)):
        if result[i] == a:
            answer.append(i+1)
    
    return answer