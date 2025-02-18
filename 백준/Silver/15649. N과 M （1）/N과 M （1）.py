# 입력 받기
N, M = map(int, input().split())
def backtrack(k):
    if k == M:  # 길이가 M인 수열이 완성되었으면 출력
        print(*arr)
        return

    for i in range(1, N + 1):  # 1부터 N까지 선택 가능
        if not isused[i]:  # 아직 사용되지 않은 숫자라면 선택
            arr[k] = i  # 현재 위치 k에 i 저장
            isused[i] = True  # 사용 표시
            backtrack(k + 1)  # 다음 숫자 선택
            isused[i] = False  # 백트래킹: 사용 취소

arr = [0] * M  # 선택된 숫자를 저장하는 배열 (길이 M)
isused = [False] * (N + 1)  # 사용 여부 확인 배열

backtrack(0)  # 백트래킹 시작