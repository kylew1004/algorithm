# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    answer = []
    dots = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                dots.append([i, j])
    
    x_dots = sorted(dots)
    y_dots = sorted(dots, key=lambda x:(x[1],[0]), reverse=True)

    answer += [x_dots[0][0], y_dots[-1][1]]
    answer += [x_dots[-1][0] + 1, y_dots[0][1] + 1]
    
    return answer
