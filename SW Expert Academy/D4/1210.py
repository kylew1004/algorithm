# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV14ABYKADACFAYh&categoryId=AV14ABYKADACFAYh&categoryType=CODE&problemTitle=%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=4&pageSize=10&pageIndex=3

for tc in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    end = 0
    for i in range(100):
        if ladder[99][i] == 2:
            end = i
    c = end
    for r in range(99, 0, -1):
        if c > 0 and ladder[r][c - 1]:
            while c > 0 and ladder[r][c - 1]:
                c -= 1
        elif c < 99 and ladder[r][c + 1]:
            while c < 99 and ladder[r][c + 1]:
                c += 1
    print('#{0} {1}'.format(tc, c))