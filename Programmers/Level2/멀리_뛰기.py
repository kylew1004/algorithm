# https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    if n < 2:
        return n

    dp = [0 for _ in range(n)]
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    answer = dp[-1] % 1234567

    return answer
