# https://www.acmicpc.net/problem/1966

t = int(input())
 
for _ in range(t):
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    tmp = [0 for _ in range(n)] 
    tmp[m] = 1 
 
    cnt = 0
    while True:
        if arr[0] == max(arr):
            cnt += 1
 
            if tmp[0] != 1:
                arr.pop(0)
                tmp.pop(0)
            else:
                print(cnt)
                break
        else:
            arr.append(arr.pop(0))
            tmp.append(tmp.pop(0))
