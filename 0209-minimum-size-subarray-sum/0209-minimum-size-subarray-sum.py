class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minusIndex = 0
        current = 0
        answer = 9999999

        for i in range(len(nums)):
            current += nums[i]
            while current >= target:
                answer = min(answer, i - minusIndex + 1)
                current -= nums[minusIndex]
                minusIndex += 1
                
        if answer == 9999999:
            answer = 0

        return answer
            