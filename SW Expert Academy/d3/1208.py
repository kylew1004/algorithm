# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=%5BS%2FW+%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0+%EA%B8%B0%EB%B3%B8%5D&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=3

for t in range(1, 11) :
    N = int(input())
    box = list(map(int, input().split()))

    for i in range(N) :
        max_index = box.index(max(box))
        min_index = box.index(min(box))
        box[max_index] -= 1
        box[min_index] += 1

    print("#{} {}".format(t, max(box)-min(box)))