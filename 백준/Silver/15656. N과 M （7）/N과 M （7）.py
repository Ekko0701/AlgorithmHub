N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
array = []
def backtracking():
    if len(array) == M:
        print(" ".join(map(str, array)))
        return

    for i in range(N):
        array.append(nums[i])
        backtracking()
        array.pop()

backtracking()