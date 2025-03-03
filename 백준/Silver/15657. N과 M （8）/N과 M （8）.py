N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
array = []
def backtracking(start):
    if len(array) == M:
        print(" ".join(map(str, array)))
        return

    for i in range(start, N):
        array.append(nums[i])
        backtracking(i)
        array.pop()

backtracking(0)