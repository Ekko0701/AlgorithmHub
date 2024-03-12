def check(data): 
    answer = 1

    for i in range(n):
        cnt = 1
        # 우측 원소와 비교
        for j in range(1, n):
            if data[i][j] == data[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt)

        cnt = 1
        # 하단 원소와 비교
        for j in range(1, n):
            if data[j][i] == data[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt)

    return answer

n = int(input())
candies = [list(input()) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
            cnt = check(candies)
            result = max(result, cnt)
            candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
        if i + 1 < n:
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
            cnt = check(candies)
            result = max(result, cnt)
            candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]

print(result)