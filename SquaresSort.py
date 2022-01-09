from typing import List
from bisect import bisect_right

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        zero = bisect_right(nums , 0)
        
        if zero == 0:
            return [pow(x,2) for x in nums]
        elif zero == len(nums):
            output = [pow(x,2) for x in reversed(nums)]
            return output

        positive = nums[zero:]
        negative = nums[0:zero]
        
        p1 = 0
        p2 = len(negative)-1
        
        squares = []
        
        if len(nums) == 1:
            return [pow(nums[0] , 2)] 

        for i in range(len(nums)):
            if p1 < len(positive) and p2 >= 0:
                posSquare = pow(positive[p1],2)
                negSquare = pow(negative[p2],2)
                
                if posSquare > negSquare:
                    squares.append(negSquare)
                    p2-=1
                else:
                    squares.append(posSquare)
                    p1+=1
            elif p1 >= len(positive):
                negSquare = pow(negative[p2],2)
                squares.append(negSquare)
                p2-=1
            elif p2 < 0:
                posSquare = pow(positive[p1],2)
                squares.append(posSquare)
                p1+=1
                

        return squares

a = [-9,-1,0,1,3]
# a = [-4,-1,0,3,10]
# a = [-5,-3,-2,-1]
# a = [0,2]

s = Solution()
print(s.sortedSquares(a))