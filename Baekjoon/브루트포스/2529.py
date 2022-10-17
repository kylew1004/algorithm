# https://www.acmicpc.net/problem/2529

def compare(n1, n2, sign):
    if sign == '>':
        return n1 > n2
    elif sign == '<':
        return n1 < n2


def dfs(cnt, num):
    global min_num, max_num
    
    if cnt == k + 1:
        if not len(min_num):
            min_num = num
        else:
            max_num = num
        return
    for i in range(10):
        if not visited[i]:
            if cnt == 0 or compare(num[-1], str(i), arr[cnt - 1]):
                visited[i] = 1
                dfs(cnt + 1, num + str(i))
                visited[i] = 0


k = int(input())
arr = list(map(str, input().split()))
visited = [0] * 10
min_num = ''
max_num = ''

dfs(0, '')

print(max_num)
print(min_num)
