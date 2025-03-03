N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * N
array = []
def backtracking(start):
    if len(array) == M:
        print(" ".join(map(str, array)))
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            array.append(nums[i])
            backtracking(i + 1)
            array.pop()
            visited[i] = False

backtracking(0)