N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False for _ in range(N)] for _ in range(N)]
total = 0
counts = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    count = 1

    while stack:
        cx, cy = stack.pop()

        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] and not visited[nx][ny]:
                    stack.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1

    return count

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            total += 1
            counts.append(dfs(i, j))

print(total)
counts.sort()

for count in counts:
    print(count)