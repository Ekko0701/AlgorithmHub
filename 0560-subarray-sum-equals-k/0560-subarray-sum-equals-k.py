class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        prefix = 0
        hashMap = {0: 1}
        for i in range(len(nums)):
            prefix += nums[i]

            if (prefix - k) in hashMap:
                answer += hashMap[prefix - k]
                
            if prefix in hashMap:
                hashMap[prefix] += 1
            else:
                hashMap[prefix] = 1

        return answer
                