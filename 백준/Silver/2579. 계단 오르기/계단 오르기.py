import sys

N = int(sys.stdin.readline())
arr = [0] + [int(sys.stdin.readline()) for i in range(1, N + 1)]
if N < 2:
    print(arr[N])
else:
    # init dp[]
    dp = [0] * (N + 1)
    # 1
    dp[1] = arr[1]
    # 2
    dp[2] = dp[1] + arr[2]
    # 3 ~ N
    for i in range(3, N + 1):
        dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i]) 
    print(dp[N])