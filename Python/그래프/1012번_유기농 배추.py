import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    visited[x][y] = True
    direction = [(0,-1), (0, 1), (-1, 0), (1, 0)]
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not visited[nx][ny] and graph[nx][ny]:
            dfs(nx, ny)

test_case = int(input())
for _ in range(test_case):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    result = 0
    for i in range(m):
        for j in range(n):
            if not visited[j][i] and graph[j][i]:
                dfs(j, i)
                result += 1
    print(result)