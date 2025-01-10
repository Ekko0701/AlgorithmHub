class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for _ in range(0, n):
            nums1.pop()
            
        for number in nums2:
            nums1.append(number)

        nums1.sort()
        