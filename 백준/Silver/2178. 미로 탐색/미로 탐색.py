from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

distance = [[-1] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(goal_x, goal_y):
    q = deque([(0, 0)])
    distance[0][0] = 0
    while q:
        x, y = q.popleft()

        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if distance[nx][ny] >= 0 or board[nx][ny] != 1:
                continue

            distance[nx][ny] = distance[x][y] + 1
            q.append((nx, ny))

    return distance[goal_x - 1][goal_y - 1] + 1

print(bfs(N,M))