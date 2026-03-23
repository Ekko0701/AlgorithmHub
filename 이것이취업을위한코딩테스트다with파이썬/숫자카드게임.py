# 문제: 숫자 카드 게임
# 여러 개의 숫자 카드가 적힌 행 중에서 하나의 행을 선택한 뒤,
# 그 행에서 가장 작은 카드를 뽑을 때 최종적으로 가장 큰 수를 구하는 문제.
# 입력:
# - 첫째 줄에 N(행의 개수), M(열의 개수)
# - 둘째 줄부터 N개의 줄에 걸쳐 각 행의 카드 숫자 M개
# 출력:
# - 각 행의 최솟값들 중 최댓값
# 예시 입력:
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
# 예시 출력:
# 2

N, M = map(int, input().split())

result = 0

for _ in range(N):
    numbers = list(map(int, input().split()))
    min_value = min(numbers)
    result = max(result, min_value)

print(result)
