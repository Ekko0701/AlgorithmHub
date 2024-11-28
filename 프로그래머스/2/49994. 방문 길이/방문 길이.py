def solution(dirs):
    current = [0, 0]
    arrays = [[[0 for _ in range(11)] for _ in range(11)] for _ in range(2)]  # 가로, 세로 이동 경로 배열
    visited_routes = set()  # 방문한 경로 저장

    moves = {
        "L": (-1, 0, 0),  # (dx, dy, idx) - idx: 가로 이동
        "R": (1, 0, 0),
        "U": (0, 1, 1),  # (dx, dy, idx) - idx: 세로 이동
        "D": (0, -1, 1),
    }

    for dir in dirs:
        dx, dy, idx = moves[dir]
        next_x, next_y = current[0] + dx, current[1] + dy

        # 경계를 벗어나는 경우 무시
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            # 경로 정보 저장
            route = ((current[0], current[1]), (next_x, next_y))
            reverse_route = ((next_x, next_y), (current[0], current[1]))

            # 양방향 경로가 방문된 적 없는 경우만 처리
            if route not in visited_routes and reverse_route not in visited_routes:
                visited_routes.add(route)  # 현재 경로 저장
                visited_routes.add(reverse_route)  # 반대 방향 경로 저장
                arrays[idx][current[0] + 5][current[1] + 5] = 1  # 시작점
                arrays[idx][next_x + 5][next_y + 5] = 1  # 끝점

            current = [next_x, next_y]  # 위치 갱신

    # 중복 없는 경로의 길이 반환
    return len(visited_routes) // 2  # 양방향 저장이므로 2로 나눔