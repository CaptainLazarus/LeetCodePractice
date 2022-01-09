from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        nonZero = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(nums[i])
            else:
                nonZero.append(nums[i])
        
        for i in range(len(nonZero)):
            nums[i] = nonZero[i]
        for i in range(len(zeros)):
            nums[i+len(nonZero)] = 0

a = [0,1,0,3,12]

s = Solution()
s.moveZeroes(a)
print(a)