n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(graph, start_node):
    need_visit, visited = [], []
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node],reverse=True))
    return visited

def bfs(graph, start_node):
    need_visit, visited = [], []
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node]))
    return visited

print(' '.join(map(str, dfs(graph, v))))
print(' '.join(map(str, bfs(graph, v))))