from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
distance = [[-1] * N for _ in range(M)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    q = deque()

    for i in range(M):
        for j in range(N):
            if board[i][j] == 1:
                q.append((i, j))
                distance[i][j] = 0

    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if distance[nx][ny] > 0 or board[nx][ny] != 0:
                continue

            distance[nx][ny] = distance[x][y] + 1
            board[nx][ny] = 1
            q.append((nx, ny))


answer = 0
bfs()
found_zero = False

for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            print(-1)
            exit()
        answer = max(answer, distance[i][j])

print(answer)