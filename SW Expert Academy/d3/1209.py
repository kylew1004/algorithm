# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

for _ in range(10) :
    T = int(input())

    array = []
    for i in range(100) :
        array.append(list(map(int, input().split())))

    max_1 = 0
    for i in range(100) :
        sum = 0
        for j in range(100) :
            sum += array[i][j]
        if sum > max_1 :
            max_1 = sum

    max_2 = 0
    for i in range(100) :
        sum = 0
        for j in range(100) :
            sum += array[j][i]
        if sum > max_2 :
            max_2 = sum

    max_3 = 0
    for i in range(100) :
        sum1 = 0 ; sum2 = 0
        sum1 += array[i][i]
        sum2 += array[i][99-i]
    if max(sum1, sum2) > max_3 :
        max_3 = max(sum1, sum2)

    print(f"#{T} {max(max_1, max_2, max_3)}")