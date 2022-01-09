from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if len(nums) == 1:
            pass
        elif len(nums) == 2:
            if k%2 == 1:
                nums[0],nums[1] = nums[1],nums[0]
            else:
                pass
        elif len(nums) >= 3:
            k = k%n
            nums.reverse()
            temp1 = nums[0:k]
            temp2 = nums[k:]
            temp1.reverse()
            temp2.reverse()
            nums1 = temp1+temp2
            for i in range(len(nums1)):
                nums[i] = nums1[i]

a = [1,2,3,4,5,6,7]
k = 3

s = Solution()
s.rotate(a,k)
print(a)
