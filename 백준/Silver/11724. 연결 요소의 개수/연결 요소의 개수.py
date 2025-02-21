import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    visited[node] = True  # 방문 처리
    for neighbor in graph[node]:  # 인접한 노드 탐색
        if not visited[neighbor]:  
            dfs(neighbor)

# 입력 받기
n, m = map(int, sys.stdin.readline().split())  # 정점 개수 n, 간선 개수 m
graph = {i: [] for i in range(1, n + 1)}  # 인접 리스트
visited = {i: False for i in range(1, n + 1)}  # 방문 배열

# 무방향 그래프 입력 받기
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프이므로 양쪽에 추가

# 연결 요소 개수 찾기
count = 0
for node in range(1, n + 1):
    if not visited[node]:  # 방문하지 않은 노드에서 DFS 시작
        dfs(node)
        count += 1  # 새로운 연결 요소 발견

print(count)