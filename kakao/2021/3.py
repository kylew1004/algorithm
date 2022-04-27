# https://tech.kakao.com/2021/07/08/2021-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-for-tech-developers-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%95%B4%EC%84%A4/

class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None

def solution(n, k, cmd):
    nodeArr = [Node() for _ in range(n)]
    for i in range(1, n):
        nodeArr[i-1].next = nodeArr[i]
        nodeArr[i].prev = nodeArr[i-1]
    
    curr = nodeArr[k]
    myStack = []

    for str in cmd:
        if str[0] == "U":
            x = int(str[2:])
            for _ in range(x):
                curr = curr.prev
        elif str[0] == "D":
            x = int(str[2:])
            for _ in range(x):
                curr = curr.next
        elif str[0] == "C":
            myStack.append(curr)
            curr.removed = True
            up = curr.prev
            down = curr.next
            if up:
                up.next = down
            if down:
                down.prev = up
                curr = down
            else:
                curr = up
        else:
            node = myStack.pop()
            node.removed = False
            up = node.prev
            down = node.next
            if up:
                up.next = node
            if down:
                down.prev = node
    answer = ''
    for i in range(n):
        if nodeArr[i].removed:
            answer += "X"
        else:
            answer += "O"
    
    return answer
                