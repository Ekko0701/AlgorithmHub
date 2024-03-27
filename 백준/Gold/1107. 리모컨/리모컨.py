goal_channel = int(input())
n = int(input())

if n > 0:
    broken_numbers = list(map(int, input().split()))
else:
    broken_numbers = []

min_count = abs(100 - goal_channel)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        if int(nums[j]) in broken_numbers:
            break
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - goal_channel) + len(nums))

print(min_count)