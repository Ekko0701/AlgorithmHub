dp = [0] * 101

dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1

T = int(input())

for _ in range(T):
    N = int(input())

    if dp[N] == 0: 
        for i in range(4, N + 1):
            if dp[i] == 0: 
                dp[i] = dp[i - 3] + dp[i - 2]

    print(dp[N])