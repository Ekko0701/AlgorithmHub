from collections import deque

M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]

count = 0
areas = []

# print(graph)

for _ in range(K):
    square = list(map(int, input().split()))
    # 직사각형 내부는 1로 변환
    for x in range(square[0], square[2]):
        for y in range(square[1], square[3]):
            graph[y][x] = 1


def bfs(sy, sx):
    area = 1

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    queue = deque([(sy, sx)])
    visited[sy][sx] = True

    while queue:
        cy, cx = queue.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[ny][nx] == 0 and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                    area += 1

    return area


for x in range(N):
    for y in range(M):
        if graph[y][x] == 0 and not visited[y][x]:
            count += 1
            areas.append(bfs(y, x))

print(count)
areas.sort()
print(' '.join(map(str, areas)))