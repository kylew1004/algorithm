# https://school.programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    answer = []
    nums = [str(i) for i in range(10)]
    
    for file in files:
        head = ""
        number = ""
        tail = ""
        for i in range(len(file)):
            if file[i] in nums:
                while i < len(file) and file[i] in nums:
                    number += file[i]
                    i += 1
                if i <= len(file):
                    tail += file[i:]
                    break
            else:
                head += file[i]
        answer.append([head, number, tail])

    answer.sort(key=lambda x:(x[0].upper(), int(x[1])))
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
    
    return answer