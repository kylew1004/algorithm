# https://school.programmers.co.kr/learn/courses/30/lessons/154538

def solution(x, y, n):
    dp = [0 for _ in range(y + 1)]

    for i in range(x + 1, y + 1):
        a, b, c = 1e6, 1e6, 1e6
        if i % 3 == 0 and i / 3 >= x:
            a = dp[i // 3]
        if i % 2 == 0 and i / 2 >= x:
            b = dp[i // 2]
        if i - n >= x:
            c = dp[i - n]
        if a == b == c == 1e6:
            dp[i] = 1e6
        else:
            dp[i] = min(a, b, c) + 1

    return dp[y] if dp[y] != 1e6 else -1