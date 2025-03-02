from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [-1] * (F + 1)

def bfs(x):
    queue = deque([x])
    visited[x] = 0
    
    while queue:
        cur = queue.popleft()

        if cur == G:
            return visited[cur]

        for move in [U, -D]:
            nx = cur + move
            if 1 <= nx <= F and visited[nx] == -1:
                visited[nx] = visited[cur] + 1
                queue.append(nx)
    return None

result = bfs(S)

if result is not None:
    print(result)
else:
    print("use the stairs")