from collections import deque
N, K = map(int, input().split())

visited = [0] * (10 ** 5 + 1) # 거리를 계산

def bfs(x):
    q = deque()
    q.append(x)

    while q:
        cur = q.popleft()
        if cur == K:
            return visited[K]
        for i in (cur + 1, cur - 1, cur * 2):
            if 0 <= i <= 10 ** 5 and not visited[i]:
                visited[i] = visited[cur] + 1
                q.append(i)


print(bfs(N))