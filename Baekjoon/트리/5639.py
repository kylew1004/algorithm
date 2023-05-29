# https://www.acmicpc.net/problem/5639

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def postorder(start, end):
    if start > end:
        return
    div = end + 1
    for i in range(start+1, end+1):
        if tree[start] < tree[i]:
            div = i
            break
    postorder(start+1, div-1)
    postorder(div, end)
    print(tree[start])
    
tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

postorder(0, len(tree)-1)