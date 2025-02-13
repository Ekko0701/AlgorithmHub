N = int(input())
cookie = [list(input().strip()) for _ in range(N)]

head_x, head_y = 0, 0

# 머리 탐색
for i in range(N):
    for j in range(N):
        if cookie[i][j] == "*":
            head_x, head_y = i + 1, j + 1  # 1-based index로 변환
            break
    if head_x != 0 and head_y != 0:
        break

# 심장의 위치 (머리 바로 아래)
heart_x, heart_y = head_x + 1, head_y

# 왼쪽 팔 길이
left_arm = 0
j = heart_y - 2  # 1-based 좌표이므로 -2로 시작
while j >= 0 and cookie[heart_x - 1][j] == "*":
    left_arm += 1
    j -= 1

# 오른쪽 팔 길이
right_arm = 0
j = heart_y  # 1-based 좌표이므로 그대로 시작
while j < N and cookie[heart_x - 1][j] == "*":
    right_arm += 1
    j += 1

# 허리 길이 (심장에서 아래 방향으로)
middle = 0
i = heart_x  # 심장의 아래에서 시작
while i < N and cookie[i][heart_y - 1] == "*":
    middle += 1
    i += 1

# 왼쪽 다리 길이 (허리 끝에서 왼쪽 아래)
left_leg = 0
i = heart_x + middle  # 허리 끝 위치
if i < N and heart_y - 2 >= 0 and cookie[i][heart_y - 2] == "*":
    while i < N and cookie[i][heart_y - 2] == "*":
        left_leg += 1
        i += 1

# 오른쪽 다리 길이 (허리 끝에서 오른쪽 아래)
right_leg = 0
i = heart_x + middle  # 허리 끝 위치
if i < N and heart_y < N and cookie[i][heart_y] == "*":
    while i < N and cookie[i][heart_y] == "*":
        right_leg += 1
        i += 1

# 결과 출력
print(heart_x, heart_y)
print(left_arm, right_arm, middle, left_leg, right_leg)