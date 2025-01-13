class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = {}
        index = 0

        while index < len(nums):
            number = nums[index]

            if number in counter:
                counter[number] += 1
            else:
                counter[number] = 1

            if counter[number] >= 3:
                for i in range(index, len(nums) - 1):
                    nums[i] = nums[i + 1]
                nums.pop()
                counter[number] = 2
            else:
                index += 1

            

            