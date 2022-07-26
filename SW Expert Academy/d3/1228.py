# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14w-rKAHACFAYD&categoryId=AV14w-rKAHACFAYD&categoryType=CODE&problemTitle=%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=3

for tc in range(1, 11):
    arr_num = int(input())
    arr = list(input().split())
    commands_num = int(input())
    commands = list(input().split())

    for c in commands:
        if c == "I":
            command = "I"
            start = "None"
            insert_num = []
            continue
        if start == "None":
            start = int(c)
            cnt = 0
            during = "None"
            continue
        if during == "None":
            during = int(c)
            continue
        if start != "None" and command == "I":
            arr.insert(start + cnt, c)
            cnt += 1

    print(f'#{tc} {" ".join(arr[0:10])}')