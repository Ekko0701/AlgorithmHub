N = int(input())
scores = [int(input()) for _ in range(N)]

count = 0

for i in range(N - 2, -1, -1):
    if scores[i] >= scores[i + 1]:
        decrease = scores[i] - scores[i + 1] + 1
        scores[i] -= decrease
        count += decrease

print(count)