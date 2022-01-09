from typing import List
from bisect import bisect_right,bisect_left

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        for i,e in enumerate(nums):
            if target - e in dic:
                return [dic[target-e] , i]
            else:
                dic[e] = i

a = [2,7,11,15]
b = 9

a = [2,3,4]
b = 6

a = [5,25,75]
b = 100


s = Solution()
print(s.twoSum(a,b))