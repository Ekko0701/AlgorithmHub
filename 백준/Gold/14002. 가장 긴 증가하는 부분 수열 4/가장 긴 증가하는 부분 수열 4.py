N = int(input())
numbers = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

result = []

order = max(dp)

for i in range(N-1, -1, -1):
    if dp[i] == order:
        result.append(numbers[i])
        order -= 1

result.reverse()
print(*result)