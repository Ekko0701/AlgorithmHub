N = int(input())

for _ in range(N):
    x = int(input())
    dp = [0] * max(4, (x + 1))
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(1, x + 1):
        if i == 1 or i == 2 or i == 3:
            continue
        else:
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

    print(dp[x])