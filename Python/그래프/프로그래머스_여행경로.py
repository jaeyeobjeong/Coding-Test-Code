from collections import defaultdict

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

def solution(tickets):
    answer = []
    routes = defaultdict(list)

    # defaultdict을 활용해 graph 생성
    for f, t in tickets:
        routes[f].append(t)

    # depart 기준 routes의 arrived를 이름순으로 정렬
    for r in routes.keys():
        routes[r].sort(reverse=True)

    stack = ['ICN']
    while stack:
        tmp = stack[-1]
        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())

    answer.reverse()

    return answer

print(solution(tickets))