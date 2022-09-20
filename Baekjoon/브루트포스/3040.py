# acmicpc.net/problem/3040

arr = [int(input()) for _ in range(9)]
flag = False

for i in range(8):
    if flag:
        break

    for j in range(i + 1, 9):
        if sum(arr) - arr[i] - arr[j] == 100:
            arr.pop(i)
            arr.pop(j - 1)

            for k in sorted(arr):
                print(k)

            flag = True
            break