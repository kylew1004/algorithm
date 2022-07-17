# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=1244&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

def dfs(idx, cnt):
    global answer

    if cnt == int(target):
        answer = max(int("".join(num)), answer)
        return
    for now in range(idx, n):
        for max_idx in range(now + 1, n):
            if num[now] <= num[max_idx]:
                num[now], num[max_idx] = num[max_idx], num[now]
                dfs(now, cnt + 1)
                num[now], num[max_idx] = num[max_idx], num[now]
    if not answer and cnt < int(target):
        rotate = (int(target) - cnt) % 2
        if rotate:
            num[-1], num[-2] = num[-2], num[-1]
        dfs(idx, int(target))


for tc in range(1, int(input()) + 1):
    num, target = input().split()
    n = len(num)
    num = list(num)
    answer = 0
    dfs(0, 0)
    print(f'#{tc} {answer}')