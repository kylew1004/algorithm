import sys
input=sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
tmp = [0] * n
cnt = 0

def mergeSort(left, right):
    global cnt
    if right - left < 1:
        return
    m = int(left + (right - left) / 2)

    mergeSort(left, m)
    mergeSort(m + 1, right)

    for i in range(left, right + 1):
        tmp[i] = arr[i]

    k = left
    idx1 = left
    idx2 = m + 1

    while idx1 <= m and idx2 <= right:
        if tmp[idx1] > tmp[idx2]:
            arr[k] = tmp[idx2]
            cnt = cnt + idx2 - k
            k += 1
            idx2 += 1
        else:
            arr[k] = tmp[idx1]
            k += 1
            idx1 += 1

    while idx1 <= m:
        arr[k] = tmp[idx1]
        k += 1
        idx1 += 1
    while idx2 <= m:
        arr[k] = tmp[idx2]
        k += 1
        idx2 += 1

mergeSort(0, n - 1)
print(cnt)
