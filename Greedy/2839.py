n = int(input())

cnt5 = n // 5

while cnt5 >= 0:
    cnt3 = (n - 5 * cnt5) // 3
    if (n == 5 * cnt5 + 3 * cnt3):
        print(cnt3 + cnt5)
        break
    else:
        cnt5 -= 1
else:
    print(-1)