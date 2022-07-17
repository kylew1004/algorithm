# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE&problemTitle=%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
# 문제 설명이 거지같다. 굳이 다시 안봐도 됨;;

for tc in range(int(input())):
    n, m = map(int, input().split())
    password = []   # 찾아야할 문자열
    decoder = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    for x in range(n):
        locked = list(map(int, input()))
        if not password:
            for i in range(m-1, -1, -1):
                if locked[i] == 1:
                    idx = i
                    for _ in range(56):
                        password.append(locked[idx])
                        idx -= 1
                    password.reverse()
                    break

    code = []   # 이진코드를 십진수로 바꿔 담는 리스트
    num = ''

    for i in range(56):
        num += str(password[i])
        if (i+1) % 7 == 0:
            for idx in range(10):
                if num == decoder[idx]:
                    code.append(idx)
                    num = ''
                    break
    
    if len(code) != 8:
        print(f'#{tc+1} 0')
    
    else:
        odd = 0
        even = 0

        for i in range(8):
            if i % 2 == 0:
                odd += code[i]
            else:
                even += code[i]
        check = 3 * odd + even
        if check % 10 == 0:
            print(f'#{tc+1} {sum(code)}')
        else:
            print(f'#{tc+1} 0')