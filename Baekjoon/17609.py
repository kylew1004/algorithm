# https://www.acmicpc.net/problem/17609

import sys
input = sys.stdin.readline

def checkPelindrome(word, left, right):
    if word == word[::-1]:
        return 0
    else:
        while left < right:
            if word[left] != word[right]:
                check_left = checkPseudo(word, left + 1, right)
                check_right = checkPseudo(word, left, right - 1)

                if check_left or check_right:
                    return 1
                else:
                    return 2
            else:
                left += 1
                right -= 1

def checkPseudo(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


for _ in range(int(input())):
    word = list(input().rstrip("\n"))
    left = 0
    right = len(word) - 1

    answer = checkPelindrome(word, left, right)
    print(answer)
