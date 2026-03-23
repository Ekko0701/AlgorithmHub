# 문제: 큰 수의 법칙
# 다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만드는 문제.
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수는 없다.
# 입력:
# - 첫째 줄에 N(수의 개수), M(더하는 횟수), K(같은 수를 연속해서 사용할 수 있는 최대 횟수)
# - 둘째 줄에 N개의 자연수
# 출력:
# - M번 더하여 만들 수 있는 가장 큰 수
# 예시 입력:
# 5 8 3
# 2 4 5 4 6
# 예시 출력:
# 46

N, M, K = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()

first = numbers[N - 1]
second = numbers[N -2]
    
second_count = M // (K + 1)
first_count = M - second_count

result = first * first_count + second * second_count

print(result)
