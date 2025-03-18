class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set()
        visited.add((entrance[0], entrance[1]))

        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]

        while queue:
            x, y, steps = queue.popleft()
            
            if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and [x, y] != entrance:
                return steps

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))

        return -1
