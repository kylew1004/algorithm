# https://www.acmicpc.net/problem/1027

def left_view(i):
    line = float('inf')
    view = 0
    idx = i - 1
    while idx >= 0:
        dx = i - idx
        dy = building[i] - building[idx]
        dydx = dy/dx

        if dydx < line:
            view += 1
            line = dydx
        idx -= 1
    return view


def right_view(i):
    line = -1 * float('inf')
    view = 0
    idx = i + 1
    while idx < n:
        dx = idx - i
        dy = building[idx] - building[i]
        dydx = dy / dx

        if dydx > line:
            view += 1
            line = dydx
        idx += 1
    return view


n = int(input())
building = list(map(int,input().split()))
idx = 0
max_view = 0

for i in range(n):
    left = left_view(i)
    right = right_view(i)
    total = left + right
    if max_view < total:
        max_view = total
        idx = i

print(max_view)
