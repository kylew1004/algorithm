# https://www.acmicpc.net/problem/1327

from collections import deque

n, k = map(int, input().split())
arr = list(input().split())
target = sorted(arr)


def bfs():
    checked = {str(arr) : 0}
    queue = deque([arr])

    while queue:
        now_arr = queue.popleft()
        if now_arr == target:
            return checked[str(now_arr)]
        for i in range(0, n - k + 1):
            new_arr = now_arr[:i] + list(reversed(now_arr[i:i + k])) + now_arr[i + k:]
            if not checked.get(str(new_arr), 0):
                checked[str(new_arr)] = checked[str(now_arr)] + 1
                queue.append(new_arr)

    return -1


print(bfs())
