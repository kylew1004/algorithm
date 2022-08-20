# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

cnt = 0
for i in reversed(range(n)):
    cnt += k // coins[i] 
    k = k % coins[i] 

print(cnt)
    