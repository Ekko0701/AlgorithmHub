from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    while queue:
        cx, cy, count = queue.popleft()

        if cx == end[0] and cy == end[1]:
            return count

        for dir in range(8):
            nx, ny = cx + dx[dir], cy + dy[dir]

            if nx < 0 or nx >= I or ny < 0 or ny >= I:
                continue
            if visited[nx][ny]:
                continue

            queue.append((nx, ny, count + 1))
            visited[nx][ny] = True

case = int(input())

for _ in range(case):
    # 한 변의 길이
    I = int(input())
    # 시작
    start = list(map(int, input().split()))
    # 도착
    end = list(map(int, input().split()))

    visited = [[False for _ in range(I)] for _ in range(I)]

    print(bfs(start[0], start[1]))