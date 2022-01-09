from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        mid = low + (high - low)//2

        if target > nums[high]:
            return len(nums)
        if target <= nums[low]:
            return 0
        
        while low < high:

            mid = low + (high - low)//2

            if target > nums[mid]:
                low = mid+1
            elif target <= nums[mid]:
                high = mid
        
        return low

a = [1,3,5,7]
b = 2

s = Solution()
print(s.searchInsert(a,b))