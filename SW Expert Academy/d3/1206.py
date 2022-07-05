# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

for tc in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))

    cnt = 0
    for i in range(2, n - 2):
        highest = max(building[i - 2], building[i - 1], building[i + 1], building[i + 2])
        if building[i] > highest:
            cnt += building[i] - highest

    print("#{} {}".format(tc, cnt))