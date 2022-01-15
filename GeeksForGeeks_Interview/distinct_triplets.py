from typing import List

class Solution:
    def findTriplets(self, nums: List[int]) -> List[int]:
        nums.sort()
        output = []
        for i in range(len(nums)-1 , 1 , -1):
            start = 0
            end = i-1
            while end > start:
                if nums[start] + nums[end] > nums[i]:
                    end-=1
                elif nums[start] + nums[end] < nums[i]:
                    start+=1
                else:
                    output.append((nums[start], nums[end] , nums[i]))
                    start+=1
                    end+=1
        return output

nums = [1,3,4,9,2,5]

s = Solution()
output = s.findTriplets(nums)
print(output)
print(len(output))