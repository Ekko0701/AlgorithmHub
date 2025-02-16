from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0
max_area = 0

def BFS(i, j):
    area = 1
    visited[i][j] = True
    queue = deque([(i, j)]) # 첫 번째 유효 노드 큐에 추가
    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] or board[nx][ny] == 0:
                continue
            visited[nx][ny] = True
            queue.append((nx, ny))
            area += 1
    return area

for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visited[i][j]:
            max_area = max(BFS(i, j), max_area)
            count += 1

print(count)
print(max_area)