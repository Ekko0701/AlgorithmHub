from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

max_rain_height = max(map(max, graph))
result = 1
island_count = 0

def bfs(x, y, height):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] > height:
                    queue.append((nx, ny))
                    visited[nx][ny] = True


for rain_height in range(max_rain_height):
    visited = [[False] * N for _ in range(N)]
    island_count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > rain_height:
                bfs(i, j, rain_height)
                island_count += 1
    result = max(result, island_count)

print(result)