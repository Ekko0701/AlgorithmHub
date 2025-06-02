from collections import deque

M, N, K = map(int, input().split())
graph = []
for _ in range(K):
    floor = []
    for _ in range(N):
        x = list(map(int, input().split()))
        floor.append(x)
    graph.append(floor)

visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(K)]

dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(queue):
    day = -1
    while queue:
        for _ in range(len(queue)):
            cx, cy, cz = queue.popleft()
            for i in range(6):
                nx, ny, nz = cx + dx[i], cy + dy[i], cz + dz[i]
                if 0 <= nx < M and 0 <= ny < N and 0 <= nz < K:
                    if not visited[nz][ny][nx] and graph[nz][ny][nx] == 0:
                        graph[nz][ny][nx] = 1
                        visited[nz][ny][nx] = True
                        queue.append((nx, ny, nz))
        day += 1
    return day

# 여러 개의 시작점을 큐에 넣고 한 번의 bfs 실행
queue = deque()
for z in range(K):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 1:
                queue.append((x, y, z))
                visited[z][y][x] = True

day = bfs(queue)

# 익지 않은 토마토가 있는지 확인
for z in range(K):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 0:
                print(-1)
                exit()

print(day)