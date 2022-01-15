# https://practice.geeksforgeeks.org/problems/subarray-with-given-total-1587115621/1
# Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

# k > 0
# n > 1

from typing import List

class Solution:
    # I don't know if mine is right, so we'll see.
    def subarraytotal(self, nums: List[int] , k: int) -> List[int]:
        start,end = 0,0
        total = 0
        i = 0
        while i <= len(nums):
            if total < k:
                total+=nums[end]
                end+=1
                i+=1
            elif total > k:
                total-=nums[start]
                start+=1
            elif total == k:
                return [start, end-1]
        return -1

    #Official Solution
    def subArraySum(self , arr, sum_):
        n= len(arr)
        curr_sum = arr[0]
        start = 0
        i = 1
        while i <= n:
            while curr_sum > sum_ and start < i-1:
            
                curr_sum = curr_sum - arr[start]
                start += 1        
            if curr_sum == sum_:
                print ("Sum found between indexes")
                print ("% d and % d"%(start, i-1))
                return 1
            if i < n:
                curr_sum = curr_sum + arr[i]
            i += 1
        print ("No subarray found")
        return 0


nums = [10, 5, 7, 1, 4, 3]
nums = [1, 4, 20, 3, 10, 5]
k = 33

s = Solution()
output = s.subarraytotal(nums,k)
# output = s.subArraySum(nums , k)
print(output)