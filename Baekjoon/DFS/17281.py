# https://www.acmicpc.net/problem/17281
# pypy3 로 컴파일 해야함!

n = int(input())
inning = [list(map(int, input().split())) for _ in range(n)]
seq = [0 for _ in range(9)]
check = [0 for _ in range(9)]

seq[3] = 0
check[3] = 1
answer = 0

def dfs(cnt):
    global answer

    if cnt == 9:
        start, score = 0, 0
        for i in inning:
            out, b1, b2, b3 = 0, 0, 0, 0
            while out < 3:
                s = seq[start]
                if i[s] == 0:
                    out += 1
                elif i[s] == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif i[s] == 2:
                    score += b2 + b3
                    b1, b2, b3 = 0, 1, b1
                elif i[s] == 3:
                    score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1
                else:
                    score += b1 + b2 + b3 + 1
                    b1, b2, b3 = 0, 0, 0

                start += 1
                start %= 9

        answer = max(answer, score)
        return

    for idx in range(9):
        if check[idx]:
            continue
        check[idx] = 1
        seq[idx] = cnt
        dfs(cnt + 1)
        check[idx] = 0
        seq[idx] = 0

dfs(1)
print(answer)