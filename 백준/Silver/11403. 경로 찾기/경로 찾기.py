import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(start):
    queue = deque([start])
    visited = [0] * n
    while queue:
        node = queue.popleft()
        for next_node in range(n):
            if graph[node][next_node] and not visited[next_node]:
                visited[next_node] = 1
                queue.append(next_node)

    return visited


result = [bfs(i) for i in range(n)]

for row in result:
    print(*row)