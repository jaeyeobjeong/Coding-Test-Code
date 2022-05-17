n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

def getParent(parent, node):
    if parent[node] == node:
        return node
    return getParent(parent, parent[node])

def unionParent(parent, node_x, node_y):
    node_x = getParent(parent, node_x)
    node_y = getParent(parent, node_y)
    if node_x < node_y:
        parent[node_y] = node_x
    else:
        parent[node_x] = node_y

def findParent(parent, node_x, node_y):
    node_x = getParent(parent, node_x)
    node_y = getParent(parent, node_y)
    if node_x == node_y:
        return True
    else:
        return False

def solution(n, costs):
    answer = 0
    count = 0

    # 초기 parent 설정 (노드 간 연결 X 상)
    parent = [0] * n
    for i in range(n):
        parent[i] = i

    # 비용 순으로 간선 정렬
    costs.sort(key = lambda x : x[2])

    for i, j, c in costs:
        # 간선 간 연결이 없을 경우, 최소 비용으로 연결
        if not findParent(parent, i, j):
            answer += c
            unionParent(parent, i, j)
            count += 1

        # 간선의 개수 : 노드의 개수 - 1
        if count == n - 1:
            break

    return answer
print(solution(n, costs))