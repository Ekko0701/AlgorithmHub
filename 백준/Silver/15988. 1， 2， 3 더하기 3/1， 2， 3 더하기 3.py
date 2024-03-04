T = int(input())
dp = [1, 2, 4, 7]
for i in range(T):
    n = int(input())
    for j in range(len(dp), n):
        dp.append((dp[j - 1] + dp[j - 2] + dp[j - 3]) % 1000000009)
    print(dp[n-1])