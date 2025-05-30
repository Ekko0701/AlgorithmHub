from collections import deque

T = int(input())

def check_graph(M, N, K):
    def bfs(x, y):
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        queue = deque([(x, y)])
        visited[x][y] = True

        while queue:
            cx, cy = queue.popleft()

            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1 :
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    graph = [[0 for _ in range(N)] for _ in range(M)]
    visited = [[False for _ in range(N)] for _ in range(M)]
    count = 0

    # 그래프 세팅
    for _ in range(K):
        x, y = map(int, input().split())

        if x < M and y < N:
            graph[x][y] = 1

    # BFS 실행
    for x in range(M):
        for y in range(N):
            if not visited[x][y] and graph[x][y] == 1:
                bfs(x, y)
                count += 1

    print(count)

for _ in range(T):
    M, N, K = map(int, input().split())
    check_graph(M, N, K)