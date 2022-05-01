# https://tech.kakao.com/2020/07/01/2020-internship-test/

from itertools import permutations

def split_expression(expression):
    tmp = []
    code = []
    for i in expression:
        if i >= '0' and i <= '9':
            tmp.append(i)
        else:
            code.append(''.join(tmp))
            tmp = []
            code.append(i)
    else:
        code.append(''.join(tmp))
    
    return code

def solution(expression):
    code = split_expression(expression)
    codes = ['*', '-', '+']
    answer = 0

    for order in permutations(codes, 3):
        tmp = code
        for operator in order:
            idx = 0
            while idx < len(tmp):
                if tmp[idx] == operator:
                    if operator == '*':
                        result = int(tmp[idx-1]) * int(tmp[idx+1]) 
                    elif operator == '+':
                        result = int(tmp[idx-1]) + int(tmp[idx+1]) 
                    elif operator == '-':
                        result = int(tmp[idx-1]) - int(tmp[idx+1])
        
                    tmp = tmp[:idx-1] + list(str(result).split()) + tmp[idx+2:]
                else:
                    idx += 1
        else:
            answer = max(answer, abs(int(tmp[0])))

    return answer

print(solution("100-200*300-500+20"))