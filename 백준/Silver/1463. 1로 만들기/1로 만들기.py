N = int(input())

dp = [0] * (N + 1) # index와 현재 숫자를 추기 위해 + 1

for i in range(2, N+1):
    # -1 연산
     dp[i] = dp[i - 1] + 1
     if i % 2 == 0:
          dp[i] = min(dp[i], dp[i//2] + 1)
     if i % 3 == 0:
          dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[N])