# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    if len(s) == 1:
        return 1
        
    for i in range(1, len(s) // 2 + 1):
        cnt = 1
        cur = ''
        temp = s[:i]
        for j in range(i, len(s), i):
            if temp == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    cur += temp
                else:
                    cur += str(cnt) + temp
                cnt = 1
                temp = s[j:j+i]
                
        if cnt == 1:
            cur += temp
        else:
            cur += str(cnt) + temp
        answer = min(answer, len(cur))
                    
    return answer