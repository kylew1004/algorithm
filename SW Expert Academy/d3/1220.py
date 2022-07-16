# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE&problemTitle=%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=3

for t in range(1, 11) :
    length = int(input())
    magnets = []
    for _ in range(length) :
        magnets.append(list(map(int, input().split())))

    count = 0
    for i in range(length) :
        state = 0
        for j in range(length) :
            if magnets[j][i] == 1 and state == 0 :
                state = 1
            elif magnets[j][i] == 2 and state == 1 :
                state = 0
                count += 1

    print("#{} {}".format(t, count))