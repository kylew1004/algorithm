# https://programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    routes = {}

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]  

    for r in routes.keys():
        routes[r].sort(reverse=True)

    st = ["ICN"]
    path = []
    
    while st:
        top = st[-1]

        if top not in routes or len(routes[top]) == 0:
            path.append(st.pop())
        else:
            st.append(routes[top][-1])
            routes[top] = routes[top][:-1]

    answer = path[::-1]
    return answer

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))