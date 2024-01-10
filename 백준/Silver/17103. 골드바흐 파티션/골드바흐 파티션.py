import sys
n = int(input())

# 소수 
M = 10**6
is_prime = [True] * (M + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(M**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, M + 1, i):
            is_prime[j] = False

for _ in range(n):
    result = 0
    n = int(input())

    for i in range(2, n // 2 + 1):
        if is_prime[i] and is_prime[n-i]:
            result += 1

    print(result)