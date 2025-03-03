N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * N
array = []
def backtracking():
    if len(array) == M:
        print(" ".join(map(str, array)))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            array.append(nums[i])
            backtracking()
            array.pop()
            visited[i] = False

backtracking()