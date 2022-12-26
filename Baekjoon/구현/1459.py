# https://www.acmicpc.net/problem/1459

x, y, w, s = map(int, input().split())

if (w * 2) < s:
    print((x + y) * w)
else:
    if abs(x - y) % 2 == 0:
        print((s * min(x, y)) + min(w, s) * abs(x - y))
    else:
        print((s * min(x, y)) + (min(w, s)* (abs(x - y) - 1) + w))
