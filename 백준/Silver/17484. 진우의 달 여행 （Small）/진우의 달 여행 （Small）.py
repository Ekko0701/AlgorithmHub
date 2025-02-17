N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1]  # 왼쪽 ↙, 아래 ↓, 오른쪽 ↘
res = float('inf')  # 최소 연료값 저장

def dfs(px, py, pd, cur):
    global res
    # 마지막 행에 도달하면 최소 연료 갱신
    if px == N - 1:
        res = min(res, cur)
        return

    # 가능한 방향 탐색
    for i in range(3):  # 3가지 방향
        ny = py + dy[i]
        if (i != pd) and (0 <= ny < M):  # 같은 방향 연속 이동 방지 + 범위 체크
            dfs(px + 1, ny, i, cur + board[px + 1][ny])  # ✅ 연료값 추가

# 0번째 행의 모든 열에서 출발하여 DFS 탐색
for i in range(M):
    dfs(0, i, -1, board[0][i])

print(res)