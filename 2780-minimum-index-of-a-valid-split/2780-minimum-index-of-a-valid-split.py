class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)

        count = Counter(nums)
        dominant = max(count, key = lambda x : count[x])
        total_count = count[dominant] 

        prefix_count = 0
        for i in range(n - 1):
            if nums[i] == dominant:
                prefix_count += 1

            left_length = i + 1
            right_length = n - left_length

            if prefix_count * 2 > left_length and (total_count - prefix_count) * 2 > right_length:
                return i

        return -1