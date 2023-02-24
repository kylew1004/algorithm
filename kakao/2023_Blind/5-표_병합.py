# https://school.programmers.co.kr/learn/courses/30/lessons/150366
'''
Union-Find => "2개의 집합의 공통 부모를 찾는 문제"에 자주 쓰임


'''
# https://school.programmers.co.kr/learn/courses/30/lessons/150366

def solution(commands):
    answer = []
    graph = [['' for _ in range(51)] for _ in range(51)]
    # parents[r][c] 는 graph[r][c]의 부모셀
    parents = [[(r, c) for c in range(51)] for r in range(51)]

    def find(r, c): # (r, c)의 최상위 부모를 찾는 함수
        if parents[r][c] == (r, c):
            return (r, c)
        else:
            pr, pc = parents[r][c]
            return find(pr, pc)

    for command in commands:
        coms = list(command.split(" "))
        if coms[0] == "UPDATE":
            length = len(coms)
            if length == 4:
                # 이미 병합이 된 경우 부모 노드 하나만 UPDATE
                r, c, value = int(coms[1]), int(coms[2]), coms[3]
                r, c = find(r, c)
                graph[r][c] = value
            else:
                value1, value2 = coms[1], coms[2]
                for r in range(1, 51):
                    for c in range(1, 51):
                        if graph[r][c] == value1:
                            graph[r][c] = value2

        elif coms[0] == "MERGE":
            r1, c1, r2, c2 = int(coms[1]), int(coms[2]), int(coms[3]), int(coms[4])
            pr1, pc1 = find(r1, c1)
            pr2, pc2 = find(r2, c2)
            if (pr1, pc1) == (pr2, pc2):
                continue
            value = graph[r1][c1] if graph[r1][c1] else graph[r2][c2]
            parents[pr2][pc2] = (pr1, pc1)
            graph[pr1][pc1] = value
            graph[pr2][pc2] = ''
            
        elif coms[0] == "UNMERGE":
            r, c = int(coms[1]), int(coms[2])
            pr, pc = find(r, c)
            value = graph[pr][pc]
            targets = []
            for _r in range(1, 51):
                for _c in range(1, 51):
                    _pr, _pc = find(_r, _c)
                    if (_pr, _pc) == (pr, pc):
                        targets.append((_r, _c))
            for _r, _c in targets:
                parents[_r][_c] = (_r, _c)
                graph[_r][_c] = ''
            graph[r][c] = value
        else:
            r, c = int(coms[1]), int(coms[2])
            r, c = find(r, c)
            answer.append(graph[r][c] if graph[r][c] else "EMPTY")
    
    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))