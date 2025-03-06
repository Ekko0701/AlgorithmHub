board = [list(input().strip()) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, group):
    stack = [(x, y)]
    visited = [[False] * 5 for _ in range(5)]
    visited[x][y] = True
    count = 1

    while stack:
        cx, cy = stack.pop()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if (nx, ny) in group and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))
                count += 1

    return count == 7


def is_valid_group(group):

    # 선택된 group이 'S'가 4명 이상인지 확인하고, 연결성을 검사

    s_count = sum(1 for x, y in group if board[x][y] == 'S')
    if s_count < 4:
        return False

    return dfs(group[0][0], group[0][1], group)


def backtrack(start, selected):
    global valid_count

    if len(selected) == 7:
        if is_valid_group(selected):
            valid_count += 1
        return

    for i in range(start, 25):
        x, y = divmod(i, 5)
        selected.append((x, y))
        backtrack(i + 1, selected)
        selected.pop()


valid_count = 0
backtrack(0, [])
print(valid_count)