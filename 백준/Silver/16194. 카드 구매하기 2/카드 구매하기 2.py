N = int(input())
dp = list(map(int, input().split()))

for i in range(0, N):
    if i == 0:
        continue
    for j in range(i, 0, -1):
        dp[i] = min(dp[i], dp[i - j] + dp[j - 1])
print(dp[N-1])