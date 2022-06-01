# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [0] * (len(words))
    
    def bfs():
        q = deque()
        q.append([begin, 0])
        answer = 0
        while q:
            word, cnt = q.popleft()
            if word == target:
                answer = cnt
                break
            for i in range(len(words)):
                temp_cnt = 0
                if not visited[i]:
                    for j in range(len(word)):
                        if word[j] != words[i][j]:
                            temp_cnt += 1
                    if temp_cnt == 1:
                        q.append([words[i], cnt+1])
                        visited[i] = 1

        return answer
    answer = bfs()
    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))