class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(array, target, isFirst):
            left = 0
            right = len(array) - 1
            
            result = -1

            while left <= right: 
                mid = (left + right) // 2

                if array[mid] == target:
                    result = mid
                    if isFirst: 
                        right = mid - 1
                    else:
                        left = mid + 1

                elif array[mid] < target:
                    left = mid + 1

                elif array[mid] > target:
                    right = mid - 1

            return result
        
        starting = binarySearch(nums, target, True)

        if starting == -1: 
            return [-1, -1]

        ending = binarySearch(nums, target, False)

        return [starting, ending]