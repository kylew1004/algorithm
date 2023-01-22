# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    answer = []
    
    terms_dic = {}
    for term in terms:
        terms_dic[term[0]] = int(term[2:]) 
    year, month, day = map(int, today.split("."))

    for i, pri in enumerate(privacies):
        tyear, tmonth, tday = pri.split(".")
        tyear = int(tyear)
        tmonth = int(tmonth)
        tday = int(tday[0:2])

        nday = tday
        nmonth = tmonth + terms_dic[pri[-1]]
        nyear = tyear

        if nmonth > 12:
            nyear += (nmonth // 12)
            if nmonth % 12 == 0:
                nyear -= 1
                nmonth = 12
            else:
                nmonth = nmonth % 12


        if nyear < year:
            answer.append(i + 1)
        elif nyear == year and nmonth < month:
            answer.append(i + 1)
        elif nyear == year and nmonth == month and nday <= day:
            answer.append(i + 1)

    return answer

print(solution("2019.01.01", ["B 12"], ["2017.12.28 B"]))
