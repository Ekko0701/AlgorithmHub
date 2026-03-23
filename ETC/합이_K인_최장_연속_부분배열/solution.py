import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

# prefix_sum의 첫 등장 인덱스를 저장
# prefix_sum[i] - prefix_sum[j] == K → 구간 [j+1, i] 합이 K
first = {0: -1}  # prefix_sum 0은 인덱스 -1에서 시작
prefix = 0
ans = 0

for i in range(N):
    prefix += A[i]
    if prefix - K in first:
        ans = max(ans, i - first[prefix - K])
    if prefix not in first:
        first[prefix] = i

print(ans)
