N = int(input())
ropes = [int(input()) for _ in range(N)]

ropes.sort(reverse=True)
result = -1

for i in range(N):
    result = max(result, ropes[i] * (i + 1))

print(result)