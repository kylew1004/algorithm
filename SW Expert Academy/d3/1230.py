# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14zIwqAHwCFAYD&categoryId=AV14zIwqAHwCFAYD&categoryType=CODE&problemTitle=%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=3

for tc in range(1, 11):
    arr_num = int(input())
    arr = list(input().split())
    commands_num = int(input())
    commands = list(input().split())

    for c in commands:
        if c == "I":
            command = "I"
            start = "None"
            insert_cnt = "None"
            continue
        elif c == "D":
            command = "D"
            del_start = -float('inf')
            continue
        elif c == "A":
            command = "A"
            add_cnt = -float('inf')
            continue

        if command == "D":
            if del_start == -float('inf'):
                del_start = int(c)
                continue
            else:
                for _ in range(int(c)):
                    del arr[del_start]
            command == "None"
        elif command == "I":
            if start == "None":
                start = int(c)
                idx_cnt = 0
                continue
            if insert_cnt == "None":
                insert_cnt = int(c)
                continue
            if insert_cnt > idx_cnt:
                arr.insert(start + idx_cnt, c)
                idx_cnt += 1
                continue
        elif command == "A":
            if add_cnt == -float("inf"):
                add_cnt = c
                idx_cnt = 0
            elif idx_cnt < add_cnt:
                arr.append(c)
                idx_cnt += 1
                continue
        command = "None"
    print(f'#{tc} {" ".join(arr[0:10])}')