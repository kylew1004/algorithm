# https://www.acmicpc.net/problem/12969

n, k = map(int, input().split())

dp = [[[[0 for _ in range(436)] for _ in range(31)] for _ in range(31)] for _ in range(31)]

ans = [0] * 31
def recursion(i, a, b, p):
    if i == n:
        if p == k:
            return True
        else:
            return False
    if dp[i][a][b][p]:
        return False
    dp[i][a][b][p] = True
    ans[i] = 'A'
    if recursion(i + 1, a + 1, b, p):
        return True
    ans[i] = 'B'
    if recursion(i + 1, a, b + 1, p + a):
        return True
    ans[i] = 'C'
    if recursion(i + 1, a, b, p + a + b):
        return True
    return False

if recursion(0, 0, 0, 0):
    print(''.join(ans[0:n]))
else:
    print(-1)