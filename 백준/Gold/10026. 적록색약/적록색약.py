from collections import deque

N = int(input())
board = [list(input().strip()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0
blindness_count = 0

def bfs(cx, cy):
    q = deque([(cx, cy)])
    visited[cx][cy] = True
    current_color = board[cx][cy]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= N or ny< 0 or ny >= N:
                continue
            if board[nx][ny] != current_color or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            q.append((nx, ny))

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count += 1
            bfs(i, j)

for i in range(N):
    for j in range(N):
        visited[i][j] = False
        if board[i][j] == "R":
            board[i][j] = "G"

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            blindness_count += 1
            bfs(i, j)

print(count, blindness_count)