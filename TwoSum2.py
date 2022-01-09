from typing import List
from bisect import bisect_right,bisect_left

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        breakPoint = bisect_left(numbers, target)
        if breakPoint >= len(numbers):
            breakPoint = len(numbers)-1

        index1 = 0
        index2 = len(numbers)-1
        
        while index1 < index2:
            sum = numbers[index1] + numbers[index2]
            if sum == target:
                return [index1+1,index2+1]
            elif sum > target:
                index2 -= 1
            else:
                index1 += 1        

a = [2,7,11,15]
b = 9

a = [2,3,4]
b = 6

a = [5,25,75]
b = 100


s = Solution()
print(s.twoSum(a,b))